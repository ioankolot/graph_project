import numpy as np
import networkx as nx 
from qaoa import QAOA
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


nelder_old_betas = False
nelder_old_gammas = False
def nelder_mead(x):
    betas=[x[0]]
    gammas=[x[1]]
    if nelder_old_betas:
        betas = nelder_old_betas + betas
        gammas = nelder_old_gammas + gammas
    graph_qaoa = QAOA(betas, gammas, number_of_qubits, 3, w, graph)
    energy = graph_qaoa.get_expected_value()
    return float(energy)

layer_2_dataset = np.load('layer_2_dataset.npy', allow_pickle=True)
old_betas = [[] for _ in range(50)]
old_gammas = [[] for _ in range(50)]
for i in range(50):
    old_betas[i].append(layer_2_dataset[i][1])
    old_betas[i].append(layer_2_dataset[i][2])
    old_gammas[i].append(layer_2_dataset[i][3])
    old_gammas[i].append(layer_2_dataset[i][4])


graph_dataset1_layer3 = [[] for _ in range(50)]
cntr = 0

for num in range(50):
    minimum_energy = 0
    graph = graph_instances[num]
    nelder_old_betas = [old_betas[num]]
    nelder_old_gammas = [old_gammas[num]]
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
    graph_dataset1_layer3[cntr].append(minimum_energy)
    graph_dataset1_layer3[cntr].append(old_betas[num])
    graph_dataset1_layer3[cntr].append(optimal_beta)
    graph_dataset1_layer3[cntr].append(old_gammas[num])
    graph_dataset1_layer3[cntr].append(optimal_gamma)
    cntr += 1

np.save('dataset_1_layer3.npy', np.array(graph_dataset1_layer3))
