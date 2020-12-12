import numpy as np
import networkx as nx


dataset1 = np.load('dataset_1.npy', allow_pickle=True)
dataset4 = np.load('dataset_4.npy', allow_pickle=True)
optimal_dataset = np.load('graphs_optimal_cost.npy')

print(optimal_dataset[:50])

for i in range(10):
    print(dataset4[i][0]/optimal_dataset[150+i])