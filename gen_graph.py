import igraph
from igraph import *

G = Graph()


with open('facebook_konect','r') as f:
	lines = f.readlines()

meta = lines[1].split()[1:]

m = int(meta[0])
n = int(meta[1])

print(m,n)

G.add_vertices(n)

for i in range(m):
    line = lines[2+i].split()
    a = int(line[0])-1
    b = int(line[1])-1
    G.add_edge(a,b)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

layout = G.layout_lgl()
plot(G, layout=layout, target=ax, vertex_size=0.5, edge_width=0.2)
plt.savefig('Graph-Facebook.png', dpi=300)

plt.show()

