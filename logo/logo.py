import networkx as nx

k = 6

cliques = [nx.complete_graph(k) for clique in range(5)]

def join(G, clique_a, clique_b):
  prefix_a = str(clique_a)+'-'
  prefix_b = str(clique_b)+'-'
  H = nx.union(cliques[clique_a], cliques[clique_b], rename=(prefix_a, prefix_b))
  H.add_edge(prefix_a+'0', prefix_b+'0')
  return nx.compose(G, H)

G = nx.Graph()
G = join(G, 0, 1)
G = join(G, 2, 1)
G = join(G, 3, 1)
G = join(G, 4, 1)

fixed_positions = {
  '0-0': (0, -1),
  '1-0': (0, 0),
  '2-0': (0, 1),
  '3-0': (0.4, -1),
  '4-0': (0.4, 1),
}
fixed_nodes = fixed_positions.keys()
pos = nx.spring_layout(G, k=0.6, iterations=1000, pos=fixed_positions, fixed=fixed_nodes)
nx.draw_networkx(G, pos, with_labels=False, node_colour='black')
for node,(x,y) in pos.items():
    G.nodes[node]['x'] = float(x)
    G.nodes[node]['y'] = float(y)
nx.write_graphml(G, 'logo.graphml')
