#!/usr/bin/env python
N, M = map(int, raw_input().split())
values = map(int, raw_input().split())
twonodes = filter(lambda x: values[x] == 2, range(N))
roots = { node for node in twonodes }

edges = filter(lambda edge: edge[0] in twonodes and edge[1] in twonodes, [map(int, raw_input().split()) for m in range(M)])

edgeMap = {}
for edge in edges:
  if edge[1] in roots:
    roots.remove(edge[1])
  edgeMap[edge[0]] = edgeMap.get(edge[0], []) + [edge[1]]

queue = [(1,[root]) for root in roots]
maxPath = (0, [])

# TODO: dynamic programming node visits to reduce complexity from complete graphs
while len(queue) != 0:
  cur = queue.pop(0)
  if cmp(maxPath, cur) < 0:
    maxPath = cur
  if cur[1][cur[0]-1] in edgeMap:
    for nextNode in edgeMap[cur[1][cur[0]-1]]:
      queue.append((cur[0]+1,cur[1]+[nextNode]))

for node in maxPath[1]:
  print(node)

