import networkx as nx

G = nx.Graph()
G.add_edges_from([('start', 'a'), ('start', 'b'), ('b', 'c'), ('b', 'j'), ('c', 'd'), ('c', 'e'), ('e', 'f'), ('e', 'g'), ('g', 'h'), ('g', 'i'), ('j', 'k'), ('k', 'r'), ('j', 'l'), ('l', 'm'), ('l', 'n'), ('m', 'k'), ('n', 'o'), ('n', 'q'), ('n', 'h'), ('k', 'x'), ('x', 'y'), ('x', 'z'), ('m', 's'), ('s', 'w'), ('s', 't'), ('t', 'u'), ('t', 'v'), ('z', 'end')])

if __name__ == "__main__":
	N = nx.dfs_preorder_nodes(G)
	dfs = list(N)
	print(dfs)