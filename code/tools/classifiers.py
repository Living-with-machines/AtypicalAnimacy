import pickle
from gensim.models.wrappers import FastText
from tools import wemb_utils
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import numpy as np
# to use it: https://github.com/charles9n/bert-sklearn
from bert_sklearn import BertClassifier
from bert_sklearn import load_model

nlp = spacy.load("en_core_web_sm")

SVM = svm.SVC(kernel = "linear", C=1,probability=True) 

wemb_model = FastText.load_fasttext_format('../models/language_models/fastai/cc.en.300.bin')

model = BertClassifier() 

def text_to_feature(texts,language_model,classifier):
    vectorizer = TfidfVectorizer()
    
    if "tfidf" in classifier:
        X = []
        for text in texts:
            doc = nlp(text)
            lemmas = " ".join([x.lemma_ for x in doc])
            X.append(lemmas)   
            
        vectorizer = language_model
        X = vectorizer.transform(X)
    
    if "wemb" in classifier:
        X = []
        for text in texts:
            x = wemb_utils.sent_embedding(text,language_model)
            X.append(x)    
        X = np.array(X)
    
    return X


def classify(path,classifier,texts,type_of_training_data,training_corpus,datascenario,prp_scenario):

    tfidf_model = None
    if classifier == "tfidf_svm":
        tfidf_model = pickle.load(open(path + "models/classifiers/" + training_corpus + datascenario + type_of_training_data + prp_scenario + "/tfidf.pkl", "rb"))

    language_models = {"tfidf_svm":tfidf_model,
                       "wemb_svm":wemb_model}

    models = {"bert":path + "models/classifiers/" + training_corpus + datascenario + type_of_training_data + prp_scenario + "/bert.bin",
              "tfidf_svm":path + "models/classifiers/" + training_corpus + datascenario + type_of_training_data + prp_scenario + "/tfidf_svm.pkl",
              "wemb_svm":path + "models/classifiers/" + training_corpus + datascenario + type_of_training_data + prp_scenario + "/wemb_svm.pkl"}
    
    model_path = models[classifier]

    if "bert" in classifier:
        model = load_model(model_path)
        X = texts
        
    else:
        model = pickle.load(open(model_path, "rb"))
        lm = language_models[classifier]
        X = text_to_feature(texts,lm,classifier) 
    
    res = model.predict_proba(X)
    res = [x[1] for x in res]
    return res