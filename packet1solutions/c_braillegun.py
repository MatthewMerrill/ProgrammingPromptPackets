braillerows = [
    [1, 2, 0],
    [1, 0, 0],
    [1, 1, 0],
    [2, 0, 0],
    [2, 1, 0],
    [1, 1, 0],
    [2, 1, 0],
    [2, 2, 0],
    [1, 2, 0],
    [1, 1, 0],
  ]

braillecols = [
    [1,2],
    [1,0],
    [2,0],
    [1,1],
    [1,2],
    [1,1],
    [2,1],
    [2,2],
    [2,1],
    [1,1],
  ]

line = raw_input().split()
N = int(line[0])
digits = map(int, list(line[1]))

rowSums = map(int, raw_input().split())

for rowIdx in range(3):
  if sum([braillerows[digit][rowIdx] for digit in digits]) != rowSums[rowIdx]:
    print("no")
    exit()

for digitIdx in range(N):
  colSums = map(int, raw_input().split())
  for colIdx in range(2):
    if braillecols[digitIdx][colIdx] != colSums[colIdx]:
      print("no")
      exit()

print("yes")

