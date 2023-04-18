# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* First member (email)
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



# Superdoku: Solving a Sudoku Puzzle

**Informal Description:**
While less of a board game and more of a paper puzzle, Sudoku is undenibly an effective way to kill an afternoon. If you need a refresher, the idea behind Sudoku is that you start with a 9x9 grid that is broken down into three rows, three columns, and three regions like so:
```
┏━┯━┯━┳━┯━┯━┳━┯━┯━┓
┠─┼─┼─╂─┼─┼─╂─┼─┼─┨
┠─┼─┼─╂─┼─┼─╂─┼─┼─┨
┣━┿━┿━╋━┿━┿━╋━┿━┿━┫
┠─┼─┼─╂─┼─┼─╂─┼─┼─┨
┠─┼─┼─╂─┼─┼─╂─┼─┼─┨
┣━┿━┿━╋━┿━┿━╋━┿━┿━┫
┠─┼─┼─╂─┼─┼─╂─┼─┼─┨
┠─┼─┼─╂─┼─┼─╂─┼─┼─┨
┗━┷━┷━┻━┷━┷━┻━┷━┷━┛
```
Initially, some of the spaces on the board are filled in with single-digit numerical values. Your goal is to fill each of the remaining spaces on the board with a value 1-9 without repeats in any row, column, or region. For example, if there is a 5 in the most top left corner, we cannot have any other 5's in the first row, first column, or the top left most 3x3 region.
It's likely that your grandparents solve the Sudoku puzzles in the daily newspaper as a form of self assessment of intelligence. Likewise, if you wish to be seen as a prodigy in their eyes you could attempt to solve a Sudoku puzzle in an impossibly fast amount of time. Luckily, we can use a depth first search (DFS) to do just that!



