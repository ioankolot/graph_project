import numpy as np
import networkx as nx

graph_instances = []

for nodes in range(10, 15):
    for seed in range(10):
        for regularity in (3, 6):
            try:
                graph_instances.append(nx.random_regular_graph(regularity, nodes, seed*10))
                graph_instances.append(nx.random_regular_graph(regularity, nodes, (seed+1)*11))
            except:
                pass


print(len(graph_instances))

graph_optimal = []
for graph in graph_instances:
    number_of_qubits = len(graph.nodes())
    w = nx.to_numpy_matrix(graph, nodelist=sorted(graph))
    best_cost_brute = 0
    for b in range(2**number_of_qubits):
        x = [int(t) for t in reversed(list(bin(b)[2:].zfill(number_of_qubits)))]
        cost = 0
        for i in range(number_of_qubits):
            for j in range(number_of_qubits):
                cost += w[i,j]*x[i]*(1-x[j])
        if best_cost_brute < cost:
            best_cost_brute = cost
    graph_optimal.append(best_cost_brute)

np.save("graphs_optimal_cost.npy", graph_optimal)