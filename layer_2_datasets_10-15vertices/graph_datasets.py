import numpy as np
import networkx as nx


dataset1 = list(np.load('dataset_1_layer2.npy', allow_pickle=True))
dataset2 = list(np.load('dataset_2_layer2.npy', allow_pickle=True))
dataset3 = list(np.load('dataset_3_layer2.npy', allow_pickle=True))
dataset4 = list(np.load('dataset_4_layer2.npy', allow_pickle=True))
optimal_dataset = np.load('graphs_optimal_cost.npy')

for k in range(10):
    dataset3.append(dataset4[k]) #the datasets are expectation value/ b0/ b1/ g0/ g1

for j in range(60):
    dataset2.append(dataset3[j])

for l in range(110):
    dataset1.append(dataset2[l])

dataset1 = np.array(dataset1)

np.save('layer_2_dataset.npy', dataset1)