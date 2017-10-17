#!/usr/bin/env python
N = input()
lines = [raw_input().split() for idx in range(N)]
towers = sorted([(int(line[0]), line[1]) for line in lines])
max_tower = towers[len(towers)-1][0]

for row in range(max_tower, 0, -1):
  print("".join(["*" if tower[0] >= row else " " for tower in towers]))

print("".join([tower[1] for tower in towers]))

