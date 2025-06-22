# Importamos lo que necesitamos.
import pandas as pd
import matplotlib.pyplot as plt
from functions import *
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize

# En primer lugar, abrimos y leemos el archivo donde se encuentra el texto.
with open('C:\\Users\\olive\\OneDrive\\Desktop\\Opiniones de alumnos\\src\\CorpusEducacion.txt', 'r') as f:
    texto = f.read()

# limpiamos el texto.
corpus = [lematizar(quitarStopwords_es(tokenizar(texto)))]

# Imprimimos el corpus final para probar.
corpus_final = []
texto_final = ""

for oracion in corpus:
    resultado = ' '.join(oracion)  # Une los elementos con un espacio
    texto_final = texto_final + ' '.join(oracion)
    corpus_final.append(resultado)

print("CORPUS\n")
print(corpus_final)

# Empezamos con la vectorización y trasformación del corpus.
vectorizer = CountVectorizer(ngram_range=(2,3), min_df=1)
X = vectorizer.fit_transform(corpus_final)

# Mostramos los N-gramas.
print("N-GRAMAS DE VECTOR")
print(vectorizer.get_feature_names_out())
pd.DataFrame(X.sum(axis=0).T,
             index=vectorizer.get_feature_names_out(),
             columns=['freq'])\
                .sort_values(by='freq', ascending=False)\
                .head(10)\
                .plot(kind='barh', title='Top 10 N-Gramas')

plt.show()
