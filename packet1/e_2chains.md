# 2 Chains

Given a DAG (directed acyclic graph) containing *N* nodes and *M* edges, find the longest path containing only "2".

Nodes hold the values, and node numbering starts at 0.

## Input

 - First line: *N* and *M*, space separated.
 - Second line: *N* nonnegative integers, representing the value of each of the *N* nodes.
 - Each of the next *M* lines: space separated nonnegative integers I, J representing an edge from I to J.

There is guaranteed to be at most one edge between any two nodes. 

## Output

The longest path containing only "2"s. If two paths contain the same count, choose the one with the smaller index in the first position. If there is still a conflict, smaller second position. (etc.)

Print each node on a new line. If no 2's exist in the graph, do not print anything.

## Constraints

```
EASY: 0 <= N <= 10
HARD: 0 <= N <= 1000

0 <= M <= N*(N-1)/2

Max Runtime: 30 seconds
```

## Sample
### Input
```
4 6
2 2 2 0
0 1
0 2
0 3
1 2
1 3
2 3
```

### Output
```
0
1
2
```
