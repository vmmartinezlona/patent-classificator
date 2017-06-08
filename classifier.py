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
Función que lee todas las etiquetas en el documento para crear una lista
en la que no se repiten las etiquetas.

return Lista de etiquetas (sección y clase)
"""
def get_labels(file):
    labels_name = []
    with open(file) as content_file:
        for line in content_file:
            words = line.split()
            labels_name.append(words[1])
    labels_name = list(set(labels_name))
    return labels_name

"""
Permite leer los archivos que contienen los datos a clasificar.
Argumentos:
    1. Archivo de datos
    2. Corpus para guardar los datos
    3. Lista para guardar los identificadores de etiquetas
    4. Lista con etiquetas en formato completo A01
"""
def read_data(file, data, labels_list, label_names):
    with open(file) as content_file:
        for line in content_file:
            words = line.split()
            text = ' '.join(word for word in words[2:] if len(word)>2 and len(word)<30)
            data.append(text)
            # Construir la etiqueta a comparar por sección y clase
            i = 0
            for label in label_names:
                if words[1]==label:
                    labels_list.append(i)
                i = i  + 1
    #print (labels_list)

# Directorios
main_dir = '/home/jaime/BACKUP/Docs/DataMining/project/'
train_file = main_dir + 'patents_train.txt'
test_file = main_dir + 'patents_test.txt'

#________________________________________________________________ Datos de entrenamiento
# # Variables para guardar los datos y las etiquetas para clasificar.
train_corpus = []
train_labels_list = []
# # Leer datos de los archivos de entrenamiento.
# # # Cargar corpus y listas de etiquetas (por nombre e identificador)
train_labels_name = get_labels(train_file)
read_data(train_file, train_corpus, train_labels_list, train_labels_name)
train_labels = np.asarray(train_labels_list)

# # Preprocesamiento
vec = TfidfVectorizer(stop_words='english', min_df=2, norm='l2')
train_corpus_fit = vec.fit_transform(train_corpus)

#________________________________________________________________ Datos de prueba
test_corpus = []
test_labels_list = []
test_labels_name = []
# # Leer datos de los archivos de entrenamiento.
# # # Cargar corpus y listas de etiquetas (por nombre e identificador)
test_labels_name = get_labels(test_file)
read_data(test_file, test_corpus, test_labels_list, test_labels_name)
test_labels = np.asarray(test_labels_list)

# # Preprocesamiento
test_corpus_fit = vec.transform(test_corpus)

#________________________________________________________________ Bayes
start = time.time()
classifier_nb = MultinomialNB().fit(train_corpus_fit, train_labels)
predicted_nb = classifier_nb.predict(test_corpus_fit)        
stop = time.time()


#Matriz de probabilidades
predicted_prob = classifier_nb.predict_proba(test_corpus_fit)
num_test_file = predicted_nb.size

output_file = main_dir + 'output.txt'
#Arreglo para guardar el identificador de patente
Id = []
#Obtener el identificador de patente de cada patente en test_file
with open(test_file, 'r', encoding = 'UTF-8') as test:
    for line in test:    
        Id.append(line.split()[0])

#Llenar el archivo de salida
with open(output_file, 'w', encoding = 'UTF-8') as file:
    for num in range(0, num_test_file):
        # Obtener los indices de los 3 elementos con mayor fitness
        sort_index = np.argsort(predicted_prob[num][:])[::-1][:3]
        #Escribir la el identidicador de patente
        data_tuple = str(Id[num]) + ' '
        for num2 in sort_index:
            #Escribir las 3 clasificaciones con mayor fitness
            predict_label = train_labels_name[num2]
            data_tuple += predict_label + ' '
        data_tuple += '\n'
        file.write(data_tuple)

#________________________________________________________________ Escribir resultados
#f = open("output.txt", "w")
#f.write('Class: ' + names[index] + str(predicted_nb[index])+'\n')

print('\n Accuracy = ' + str(np.mean(predicted_nb == test_labels)))
print('\nconfusion matrix:')
print(metrics.confusion_matrix(test_labels, predicted_nb))
print('\nPerformance:')
print(metrics.classification_report(test_labels, predicted_nb, target_names=label_names))
print('\n\n')
print('Training + test_time = ' + str(stop-start))
