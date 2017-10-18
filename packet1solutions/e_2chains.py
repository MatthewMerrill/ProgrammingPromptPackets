#!/usr/bin/env python
N, M = map(int, raw_input().split())
values = map(int, raw_input().split())
twonodes = filter(lambda x: values[x] == 2, range(N))
roots = { node for node in twonodes }

edges = filter(lambda edge: edge[0] in twonodes and edge[1] in twonodes, [map(int, raw_input().split()) for m in range(M)])

edgeMap = {}
parentMap = {}
for edge in edges:
  if edge[0] in twonodes and edge[1] in twonodes:
    if edge[1] in roots:
      roots.remove(edge[1])
    edgeMap[edge[0]] = edgeMap.get(edge[0], []) + [edge[1]]
    parentMap[edge[1]] = parentMap.get(edge[1], []) + [edge[0]]

visitedFrom = {}
maxDyn = {}
queue = [root for root in roots]
maxPath = (0, [])

for node in twonodes:
  maxDyn[node] = (-1, [node]) if node in roots else (0, [])
  visitedFrom[node] = []

while len(queue) != 0:
  curNode = queue.pop(0)
  if curNode in edgeMap:
    for nextNode in edgeMap[curNode]:
      maxDyn[nextNode] = min(maxDyn[nextNode], (maxDyn[curNode][0] - 1, maxDyn[curNode][1] + [nextNode]))
      if curNode not in visitedFrom[nextNode]:
        visitedFrom[nextNode] += [curNode]
      if len(visitedFrom[nextNode]) == len(parentMap[nextNode]):
        queue.append(nextNode)
  elif cmp(maxPath, maxDyn[curNode]) > 0:
    maxPath = maxDyn[curNode]

for node in maxPath[1]:
  print(node)

