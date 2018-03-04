# TODO: write without NetworkX

import networkx as nx
import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))
E = []

for _ in range(M):
    (x, y) = map(int, input().split())
    E.append((x,y))

E = list(E)

G = nx.Graph()
G.add_nodes_from(range(N))
G.add_edges_from(E)
for i in range(N):
    G.nodes[i]['weight'] = A[i]

n_comp = nx.number_connected_components(G)

if n_comp == 1: # G is a tree
    print(0)

else:
    subgraphs = list(nx.connected_component_subgraphs(G)) # list of connected components
    comp_vertices = [nx.number_of_nodes(g) for g in subgraphs]
    if max(comp_vertices) <  n_comp - 1:
        print("Impossible")
    else:
        subgraph_v_weight = []
        for i in range(n_comp):
            v_subgraph = list(nx.nodes(subgraphs[i])) # list of vertices in the i-th subgraph
            lst = [(j, subgraphs[i].nodes[j]['weight']) for j in v_subgraph]
            subgraph_v_weight.append(sorted(lst, key=lambda tup:tup[1])) # sort by vertex weight

        '''
        subgraph_v_weight[i][j]:
            The tuple (v, w), where v is in i-th subgraph and has j-th smallest weight.
        '''

        # initialize
        val = 0

        for _ in range(n_comp-1):
            cand = np.array([lst[0][1] if lst != [] else np.inf for lst in subgraph_v_weight]) # lst[0][1]: the minimum weight in a component
            arg = np.argsort(cand)
            val += cand[arg[0]] + cand[arg[1]]
            subgraph_v_weight[arg[0]].pop(0)
            subgraph_v_weight[arg[1]].pop(0)

        print(val)
