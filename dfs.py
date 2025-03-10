import networkx as nx

G = nx.Graph()
G.add_edges_from([('start', 'a'), ('start', 'b'), ('b', 'c'), ('b', 'j'), ('c', 'd'), ('c', 'e'), ('e', 'f'), ('e', 'g'), ('g', 'h'), ('g', 'i'), ('j', 'k'), ('k', 'r'), ('j', 'l'), ('l', 'm'), ('l', 'n'), ('m', 'k'), ('n', 'o'), ('n', 'q'), ('n', 'h'), ('k', 'x'), ('x', 'y'), ('x', 'z'), ('m', 's'), ('s', 'w'), ('s', 't'), ('t', 'u'), ('t', 'v'), ('z', 'end')])

#G.add_edges_from([('start', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('d', 'e'), ('d', 'f'), ('f', 'g'), ('f', '6'), ('g', 'h'), ('g', 'i'), ('f', 'j'), ('j', 'z'), ('j', 'v'), ('v', 'x'), ('v', 'w'), ('w', 'y'), ('w', 'z'), ('w', 'j'), ('v', 'u'), ('u', 't'), ('u', '3'), ('u', '1'), ('1', '2'), ('1', '4'), ('4', '5'), ('4', 'c'), ('b', 'k'), ('k', 'l'), ('k', 'm'), ('m', '0'), ('m', 'n'), ('n', 'o'), ('n', 'p'), ('n', 't'), ('0', 'q'), ('q', 't'), ('q', 'r'), ('q', 's'), ('z', 'end')])

if __name__ == "__main__":
	N = nx.dfs_preorder_nodes(G)
	dfs = list(N)
	print(dfs)