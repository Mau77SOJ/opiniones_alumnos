import spacy
import string
from nltk.corpus import stopwords

nlp = spacy.load("es_core_news_sm")

def tokenizar(texto):
    doc = nlp(texto)
    tokens = [token.text for token in doc if not token.is_space and not token.is_punct]
    return tokens

def quitarStopwords_es(texto):
    ingles = stopwords.words("spanish")
    texto_limpio = [w.lower() for w in texto if w.lower() not in ingles 
                    and w not in string.punctuation 
                    and w not in ["'s", '|', '--', "''", "``", "-", ".-", ".", "sí", "no", "año", "años", "etc", "etc.", "-"]]
    return texto_limpio

def lematizar(texto):
    doc = nlp(" ".join(texto))  # pasamos texto como string a spaCy
    texto_lema = []
    for token in doc:
        # Solo agregamos tokens que no sean espacios o puntuación
        if not token.is_punct and not token.is_space:
            texto_lema.append(token.lemma_.lower())
    return texto_lema