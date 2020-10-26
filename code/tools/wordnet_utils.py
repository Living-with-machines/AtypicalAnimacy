from sentence_transformers import SentenceTransformer
import torch,scipy
from nltk.corpus import wordnet as wn
from tools import wemb_utils
from gensim.models.wrappers import FastText
from pathlib import Path

# sent_sim_model = SentenceTransformer('models/bert-base-nli-mean-tokens')

# wemb_model = FastText.load_fasttext_format('models/language_models/cc.en.300.bin')

def wordnet_animacy(token,sentence,wsd,tokenizer):

    # Token is animate if all senses are living things; token is inanimate if no senses are living things:
    hypernyms = lambda s: s.hypernyms()
    word_senses = wn.synsets(token)
    
    personal_pronouns = ["i", "you", "he", "she", "we", "me", "him", 
                         "her", "us", "myself", "yourself", "himself", 
                         "herself", "ourselves", "yourselves"]
    
    if token.lower() in personal_pronouns:
        return 1
    
    if not word_senses:
        return None
    
    else:
        all_living = True
        all_dead = True
        for ws in word_senses:
            ws_hypernyms = [hyp.name() for hyp in list(ws.closure(hypernyms))]
            if not 'living_thing.n.01' in ws_hypernyms:
                all_living = False
            if 'living_thing.n.01' in ws_hypernyms:
                all_dead = False

        if all_living == True:
            return 1
        elif all_dead == True:
            return 0
    
        # Otherwise, determine animacy by select best synset:
        if wsd is "bert":
            word_sense = bert_lesk_wsd(token,sentence)

        if wsd is "wemb":
            word_sense = w2v_lesk_wsd(token,sentence)

        else:
            word_sense = wn.synsets(token)[0]

        hypernyms = lambda s: s.hypernyms()
        hypernyms_word_sense = [x.name() for x in list(word_sense.closure(hypernyms))]

        if 'living_thing.n.01' in hypernyms_word_sense:
            return 1
        else:
            return 0




def w2v_sim_ranking(token,sentence,corpus,labels,wemb_model):
    
    proc_corpus = [" ".join([tok for tok in sent.split(" ")  if tok!=token]) for sent in corpus]
    proc_sentence = " ".join([tok for tok in sentence.split(" ")  if tok!=token])
    
    sent_embedding = wemb_utils.sent_embedding(proc_sentence,wemb_model).reshape(1,-1)
    
    results = []
    
    for x in range(len(proc_corpus)):
        label = labels[x]
        orig_gloss = corpus[x]
        proc_gloss = proc_corpus[x]
        
        gloss_embedding = wemb_utils.sent_embedding(proc_gloss,wemb_model).reshape(1,-1)
        try:
            sim = 1.0 - scipy.spatial.distance.cdist(sent_embedding, gloss_embedding, "cosine")[0]
            results.append([label,orig_gloss,sim])
        except Exception as e:
            print (e)
            print (results.append([label,orig_gloss]))
            results.append([label,orig_gloss,sim,0.0])
            continue
        
        
    results.sort(key=lambda x: x[2],reverse=True)

    return results

    
    
def bert_sim_ranking(token,sentence,corpus,labels,sent_sim_model):
    
    proc_corpus = [" ".join([tok for tok in sent.split(" ")  if tok!=token]) for sent in corpus]
    proc_sentence = " ".join([tok for tok in sentence.split(" ")  if tok!=token])
    
    sent_embedding = sent_sim_model.encode([proc_sentence])
    
    results = []
    
    for x in range(len(proc_corpus)):
        label = labels[x]
        orig_gloss = corpus[x]
        proc_gloss = proc_corpus[x]
        
        gloss_embedding = sent_sim_model.encode([proc_gloss])
        try:
            sim = 1.0 - scipy.spatial.distance.cdist(sent_embedding, gloss_embedding, "cosine")[0]
            results.append([label,orig_gloss,sim])
        except Exception as e:
            print (e)
            print (results.append([label,orig_gloss]))
            results.append([label,orig_gloss,sim,0.0])
            continue
        
        
    results.sort(key=lambda x: x[2],reverse=True)

    return results


def bert_lesk_wsd(token,sentence):
    synsets = wn.synsets(token)
    glosses = [syn.definition() for syn in synsets]
        
    pred= bert_sim_ranking(token,sentence,glosses,synsets,sent_sim_model)
    
    best_sense = pred[0][0]
    
    return best_sense

def w2v_lesk_wsd(token,sentence):
    synsets = wn.synsets(token)
    glosses = [syn.definition() for syn in synsets]
        
    pred= w2v_sim_ranking(token,sentence,glosses,synsets,wemb_model)
    
    best_sense = pred[0][0]
    
    return best_sense