import numpy as np
import networkx as nx


dataset1 = np.load('dataset_1.npy', allow_pickle=True)
dataset2 = np.load('dataset_2.npy', allow_pickle=True)
dataset3 = np.load('dataset_3.npy', allow_pickle=True)
dataset4 = np.load('dataset_4.npy', allow_pickle=True)
optimal_dataset = np.load('graphs_optimal_cost.npy')

for k in range(10):
    dataset3[50+k] = dataset4[k]

for j in range(60):
    dataset2[50+j] = dataset3[j]

for l in range(110):
    dataset1[50+l] = dataset2[l]


kol = np.load('layer_1_dataset.npy', allow_pickle=True)

print(-20.66/optimal_dataset[45])