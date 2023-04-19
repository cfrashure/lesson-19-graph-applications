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
G.add_edges_from([(0, 1), (0,2), (2, 3), (2, 10), (3, 4), (3, 5), (5, 6), (5, 7), (7, 8), (7, 9), (10, 11), (11, 18), (10, 12), (12, 13), (12, 14), (13, 11), (14, 15), (19, 17), (19, 8), (11, 24), (24, 25), (24, 26), (13, 18), (18, 22), (18, 19), (19, 20), (19, 21), (26, 27)])
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
[0, 1, 2, 3, 4, 5, 6, 7, 8, 19, 17, 18, 11, 10, 12, 13, 14, 15, 24, 25, 26, 27, 22, 20, 21, 9]
```

**Interpretation of Results:**


