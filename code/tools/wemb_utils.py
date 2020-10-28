import nltk
import numpy as np

def sent_embedding(text,emb_model):
    
    text = nltk.tokenize.WordPunctTokenizer().tokenize(text)
    
    text = [token for token in text if token.isalpha()]
    
    doc_embed = []
    
    for word in text:
            try:
                embed_word = emb_model[word]
                doc_embed.append(embed_word)
            except KeyError:
                continue
                
    if len(doc_embed)>0:
        avg = [float(sum(col))/len(col) for col in zip(*doc_embed)]

        avg = np.array(avg)

        return avg
    else:
        return np.zeros(emb_model.vector_size)