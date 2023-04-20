# Gnarly Graphs

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* Colby Frashure (cfrashur@udel.edu)
* Andrew Roberts (andrewzr@udel.edu)
* Third member (email)
* Fourth member (email)

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# First Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]


**Setup code**:

```python
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:

# Buzz-worthy Maze: Find Your Way In

**Informal Description:**
Mazes have been a challenging source of entertainment for people of all ages for centuries. From the childhood joy of solving mazes in puzzle books to haunted houses and corn mazes, we all have some memory associated with mazes. Here we have a buzz-worthy maze from the back of a box of Cheerios. Our objective is to find a way from the outside to the center of the honey spilled by the menacing bee.

![Image of original maze](./maze.png)
*I've taken the liberty of labeling each vertex with a letter*

>**Formal Description:**
> * Input: An unweighted, undirected graph G = (V, E), s, where V is the set of verticies (maze junctions), E is the set of edges (paths connecting junctions), and s being the starting vertex in V.
> * Output: A set of verticies in V representing the path out of the maze

**Graph Problem/Algorithm:** DFS

**Setup Code:**

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([('start', 'a'), ('start', 'b'), ('b', 'c'), ('b', 'j'), ('c', 'd'), ('c', 'e'), ('e', 'f'), ('e', 'g'), ('g', 'h'), ('g', 'i'), ('j', 'k'), ('k', 'r'), ('j', 'l'), ('l', 'm'), ('l', 'n'), ('m', 'k'), ('n', 'o'), ('n', 'q'), ('n', 'h'), ('k', 'x'), ('x', 'y'), ('x', 'z'), ('m', 's'), ('s', 'w'), ('s', 't'), ('t', 'u'), ('t', 'v'), ('z', 'end')])
```

**Visualization:**
![DFS Graph of Maze](./DFS-maze-graph.png)

**Solution Code:**

```python
N = nx.dfs_preorder_nodes(G)
dfs = list(N)
print(dfs)
```

**Output**

```
['start', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'n', 'l', 'j', 'k', 'r', 'm', 's', 'w', 't', 'u', 'v', 'x', 'y', 'z', 'end', 'o', 'q', 'i']
```

**Interpretation of Results:**
This list shows the order that the DFS algorithim took as it searched the paths in the in the maze starting at the 'start' vertex. Since this is a pre-order search, it always tries the leftmost vertex first before backtracking and trying the other vertex. From this output we see that starting at the 'start' vertex it attempted to go the route of 'a' only to find that it was a dead end so it backtracked and moved to the 'b' vertex which branches from 'start'. It searches the verticies accessible down a path until it reaches a dead end like it did with 'i' and backtracks to the previous split that it didn't search.

