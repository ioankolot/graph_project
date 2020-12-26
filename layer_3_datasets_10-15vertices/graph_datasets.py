import numpy as np
import networkx as nx


dataset1 = list(np.load('dataset_1_layer3.npy', allow_pickle=True))
dataset2 = list(np.load('dataset_2_layer3.npy', allow_pickle=True))
dataset3 = list(np.load('dataset_3_layer3.npy', allow_pickle=True))
optimal_dataset = np.load('graphs_optimal_cost.npy')


for j in range(50):
    dataset2.append(dataset3[j])

for l in range(100):
    dataset1.append(dataset2[l])

dataset1 = np.array(dataset1)


np.save('layer_3_dataset.npy', dataset1)