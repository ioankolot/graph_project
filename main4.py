import numpy as np
import networkx as nx 
from qaoa import QAOA
import graphs
import scipy.optimize
import random


graph_instances = []

for nodes in range(10, 15):
    for seed in range(10):
        for regularity in (3, 6):
            try:
                graph_instances.append(nx.random_regular_graph(regularity, nodes, seed*10))
                graph_instances.append(nx.random_regular_graph(regularity, nodes, (seed+1)*11))
            except:
                pass


def nelder_mead(x):
    betas=[x[0]]
    gammas=[x[1]]
    graph_qaoa = QAOA(betas, gammas, number_of_qubits, 1, w, graph)
    energy = graph_qaoa.get_expected_value()
    return float(energy)

layer_1_dataset = np.load('layer_1_dataset.npy', allow_pickle=True)
old_betas = []
old_gammas = []
for i in range(150,160):
    old_betas.append(layer_1_dataset[i][1])
    old_gammas.append(layer_1_dataset[i][2])

graph_dataset4_layer1 = [[] for _ in range(10)]
cntr = 0

for num in range(150,160):
    minimum_energy = 0
    graph = graph_instances[num]
    for beta in np.linspace(0, np.pi, 6):
        for gamma in np.linspace(0, 2*np.pi, 10):
            number_of_qubits = len(graph.nodes())
            w = nx.to_numpy_matrix(graph, nodelist=sorted(graph.nodes()))
            minimum_energy_object = scipy.optimize.minimize(nelder_mead, x0=(beta, gamma), method='Nelder-Mead')
            if minimum_energy_object.fun < minimum_energy:
                minimum_energy = minimum_energy_object.fun
                optimal_beta = minimum_energy_object.x[0]
                optimal_gamma = minimum_energy_object.x[1]
                print('{}'.format(cntr))
    print("For the {} graph with Nelder Mead the minimum energy is {} with optimal beta:{} and optimal gamma: {}".format(cntr, minimum_energy, optimal_beta, optimal_gamma))           
    graph_dataset4_layer1[cntr].append(minimum_energy)
    graph_dataset4_layer1[cntr].append(optimal_beta)
    graph_dataset4_layer1[cntr].append(optimal_gamma)
    cntr += 1

np.save('dataset_4_layer1.npy', np.array(graph_dataset4_layer1))


