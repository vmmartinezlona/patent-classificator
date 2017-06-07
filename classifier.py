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


def read_data(file, data, label, label_names):
    with open(file) as content_file:
        for line in content_file:
            words = line.split()
            text = ' '.join(word for word in words[1:] if len(word)>2 and len(word)>30)
            data.append(text)
            for num in range(0,7):
                if words[0]==label_names[num]:
                    label.append(num)

main_dir = '/home/jaime/BACKUP/Docs/DataMining/project/'
train_file = main_dir + 'patents_train.txt'
#val_file = main_dir + 'patents_validation.txt'
test_file = main_dir + 'patents_test.txt'
label_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
corpus = []
labels_list = []

read_data(train_file, corpus, labels_list, label_names)

labels = np.asarray(labels_list)

vec.TfidfVectorizer(stop_words='english', min_df=2, norm='l2')
corpus_fit = vec.fit_transform(corpus)

test_corpus = []
test_labels_list = []

read_data(test_file, test_corpus, test_labels_list, label_names)
test_labels = np.asarray(test_labels_list)

test_fit = vec.transform(test_corpus)

start = time.time()
clf_nb = MultinomialNB().fit(corpus_fit, labels)
predicted_nb = clf_nb.predict(test_fit)
stop = time.time()

print('\n Accuracy = ' + str(np.mean(predicted_nb == test_labels)))
print('\nconfusion matrix:')
print(metrics.confusion_matrix(test_labels, predicted_nb))
print('\nPerformance:')
print(metrics.classification_report(test_labels, predicted_nb, target_names=label_names))
print('\n\n')
print('Training + test_time = ' + str(stop-start))
