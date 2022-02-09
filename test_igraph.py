import igraph
from igraph import *
import random

G = Graph()

G.add_vertices(10)
for i in range(23):
    u = random.randrange(0,10)
    v = random.randrange(0,10)
    print(u,v)
    if u==v : continue
    G.add_edge(u, v)

G.es['weight'] = [random.randrange(0.0,1000.0) for i in range(len(G.es))]

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

layout = G.layout_lgl()
plot(G, layout=layout, target=ax)

plt.show()

print(G.es['weight'])

