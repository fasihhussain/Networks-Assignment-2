import networkx as nx
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

    def average_clustering_coefficient(self):
        """Calculates average clustering coefficient of the graph G

        Returns:
        Returns the average clustering coefficient
        """
        return nx.algorithms.cluster.average_clustering(self.G)

    def average_path_length(self):
        """Calculates average path length of the graph G

        Returns:
        float: Average path length in graph G
        """
        return nx.average_shortest_path_length(self.G)

    def degrees(self):
        """Returns degree of all vertices in the graph

        Returns:
            [int]: array of degrees of vertices
        """
        return list(map(lambda x: x[1], self.G.degree(range(self.n))))
