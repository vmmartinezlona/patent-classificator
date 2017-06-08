# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 10:15:04 2017

@author: JC
"""

def read_classes(file, data):
    with open(file) as f_input:
        for line in f_input:
            tokens = line.rstrip().split()
            classes = [token for token in tokens[1:]]
            pn = tokens[0]
            data[pn]=classes    

input_dir = 'C:/Users/JC/Documents/UG/Cursos/licenciatura/2017/ene_junio/Mineria de datos/data/final_project/'
gt_file = input_dir+'ground_truth.txt'
gt = {}
read_classes(gt_file, gt)

results_file = input_dir+'results.txt'
results = {}
read_classes(results_file, results)

top = 0
three = 0
all_g = 0
n_patents = len(gt)
for key,val in results.items():
    mc = gt[key][0]
    guess1 = val[0]
    if guess1==mc:
        top+=1
    if mc in val:
        three+=1
    if guess1 in gt[key]:
        all_g+=1

top = top/n_patents
three = three/n_patents
all_g = all_g/n_patents

print('Top accuracy = ',top)
print('Three accuracy = ',three)
print('All accuracy = ',all_g)