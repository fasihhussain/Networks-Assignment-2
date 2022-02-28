import networkx as nx
import numpy as np

# import matplotlib.pyplot as plt
from random import random


class ErdosRenyi:
    def __init__(self, n, p):
        """Initializes an Erdos-Renyi graph

        Args:
            n (int): Number of nodes in the graph
            p (float): Probability of connection between any two nodes
        """
        self.G = nx.Graph()
        self.n = n
        self.p = p

        self.G.add_nodes_from(range(self.n))

        for i in range(n):
            for j in range(i + 1, n):
                if random() < self.p:
                    self.G.add_edge(i, j)

    def get_clustering_coefficient(self, nodes=None):
        """Calculates clustering coefficient in graph G

        Args:
            nodes: Nodes of graph G. Defaults to None.

        Returns:
            Returns the clustering coefficient of the given nodes, if none then returns their average
        """
        return nx.algorithms.cluster.clustering(G, nodes)

    def get_average_path_length(self):
        """Calculates average path length of the graph G

        Returns:
            float: Average path length in graph G
        """
        return nx.average_shortest_path_length(self.G)

    def get_degree_distribution(self):
        degrees = list(self.G.degree(range(self.n)))
        max_degree = max(degrees, key=lambda x: x[1])[1]
        histogram = np.zeros(max_degree)

        for node, degree in degrees:
            histogram[degree] += 1
        return histogram


G = ErdosRenyi(7000000, 0.01)
print(f"Average Clustering Coefficient: {G.get_clustering_coefficient()}")
print(f"Average Path Length: {G.get_average_path_length()}")
