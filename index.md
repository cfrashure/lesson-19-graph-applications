# Gaming Graphs: Graph Algorithms with Tabletop/Board Games

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* Colby Frashure (cfrashur@udel.edu)
* Second member (email)
* Third member (email)
* Fourth member (email)

The tradition of board games dates back millennia and has been enjoyed by countless generations.
On the other hand, modern graph theory has only developed over the last couple of centuries.
However, as we will demonstrate, the two are more connected than you think; we can use graph
theory to look at and solve our favorite timeless games in brand-new ways. In many ways,
the problems mirror the topic: Like a board game connecting the young and old generations, we
shall connect this ancient pass time with modern theory.

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# Tricky Terrain: Shortest Path to the Goal!

**Informal Description**:  
Imagine you have an 8x8 board, with a game piece you must move from one spot of the board to another.
Each space has one of three possible terrains with an associated moving value (MV):
1. Land: Cost 1MV. There are 32 land terrains that can be assigned.
2. Hill: Cost 2MV. There are 16 hill terrains that can be assigned.
3. Mountain: Cost 3MV. There are 16 mountain terrains that can be assigned.
Your objective is to move from the starting spot to the end spot whilst traversing
the least treacherous terrain, or, in other words, with the smallest MV.
You can assume the position of each spot is given a random terrain at the start of the game, so no
planning out your route beforehand! Thankfully, we can use Dijkstra's Algorithm to find the shortest
path from start to finish whilst minimizing our MV! Neat!

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: Single Source Shortest Path (Dijkstra's Algorithm)


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

