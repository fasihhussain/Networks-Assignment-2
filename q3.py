import networkx as nx

n = 50
d = 6

G = nx.Graph()
G.add_nodes_from(range(n))

for node in range(n):
    for i in range(1, 1 + d // 2):
        G.add_edge(node, (node + i) % n)

print(nx.algorithms.cluster.average_clustering(G))
nx.draw(G)
