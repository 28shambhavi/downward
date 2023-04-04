# given a graph of temporally ordered tasks, find the optimal task allocation for n agents

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import itertools

def get_task_allocation(G, n_agents):
    total_tasks = len(G.nodes())

    # if node has no incoming edges, it is a root node
    root_nodes = [node for node in G.nodes() if G.in_degree(node) == 0]
    print("root nodes: ", root_nodes)

    # allocate tasks to agents starting from root nodes in a greedy manner

    

def main():
    G = nx.DiGraph()
    G.add_nodes_from([1,2,3,4,5,6,7,8]) 
    G.add_edges_from([(1,4),(2,3),(3,5),(2,8),(7,8),(6,7),(3,8),(3,4)])

    get_task_allocation(G, 2)


    # draw the graph
    # pos = nx.spring_layout(G)
    # nx.draw_networkx_nodes(G, pos)
    # nx.draw_networkx_edges(G, pos)
    # nx.draw_networkx_labels(G, pos)
    # plt.show()

if __name__ == '__main__':
    main()