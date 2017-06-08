#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 11:29:15 2017

@author: jaime
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import numpy as np
import time

"""
Permite leer los archivos que contienen los datos a clasificar.
Argumentos:
    1. Archivo de datos
    2. Corpus para guardar los datos
    3. Lista para guardar los identificadores de etiquetas
    4. Lista con las etiquetas de cada sección (A)
    5. Lista con las etiquetas de cada clase (01)
    6. Lista con etiquetas en formato completo A01
"""
def read_data(file, data, labels_list, section_labels, class_labels, label_names):
    with open(file) as content_file:
        for line in content_file:
            words = line.split()
            text = ' '.join(word for word in words[2:] if len(word)>2 and len(word)<30)
            data.append(text)
            # Construir la etiqueta a comparar por sección y clase
            for letter in range(0, 8):
                for num in range(0, 10):
                    for num2 in range(0, 10):
                        label = section_labels[letter] + class_labels[num] + class_labels[num2]
                        if words[1]==label:
                            label_names.append(label)
                            labels_list.append(num)

# Directorios
main_dir = '/home/jaime/BACKUP/Docs/DataMining/project/'
train_file = main_dir + 'patents_train.txt'
test_file = main_dir + 'patents_test.txt'
# # Para etiquetas (por sección y clase)
section_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
class_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
label_names = []

#________________________________________________________________ Datos de entrenamiento
# # Variables para guardar los datos y las etiquetas para clasificar.
train_corpus = []
train_labels_list = []
# # Leer datos de los archivos de entrenamiento.
# # # Cargar corpus y listas de etiquetas (por nombre e identificador)
read_data(train_file, train_corpus, train_labels_list, section_labels, class_labels, label_names)

train_labels = np.asarray(train_labels_list)

# # Preprocesamiento
vec = TfidfVectorizer(stop_words='english', min_df=2, norm='l2')
train_corpus_fit = vec.fit_transform(train_corpus)

#________________________________________________________________ Datos de prueba
test_corpus = []
test_labels_list = []
# # Leer datos de los archivos de entrenamiento.
# # # Cargar corpus y listas de etiquetas (por nombre e identificador)
read_data(test_file, test_corpus, test_labels_list, section_labels, class_labels, label_names)
test_labels = np.asarray(test_labels_list)

# # Preprocesamiento
test_corpus_fit = vec.transform(test_corpus)

#________________________________________________________________ Bayes
start = time.time()
classifier_nb = MultinomialNB().fit(train_corpus_fit, train_labels)
predicted_nb = classifier_nb.predict(test_corpus_fit)
stop = time.time()

print('\n Accuracy = ' + str(np.mean(predicted_nb == test_labels)))
print('\nconfusion matrix:')
print(metrics.confusion_matrix(test_labels, predicted_nb))
print('\nPerformance:')
print(metrics.classification_report(test_labels, predicted_nb, target_names=label_names))
print('\n\n')
print('Training + test_time = ' + str(stop-start))
