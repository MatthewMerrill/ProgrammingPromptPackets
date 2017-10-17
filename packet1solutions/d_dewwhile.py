#!/usr/bin/env python
N = input()

for n in range(N):
  X, T = map(int, raw_input().split())
  T -= 5
  while T >= 0:
    T -= 1
    if abs(X) % 7 == 0:
      X = (X - 7) // 2
    else:
      X = 2 * X - 1
    if X % 5 == 0:
      break
  print("yes" if T >= 0 else "no")

