H, W, D = map(int, input().split())
position = {}

for i in range(H):
    row = list(map(int, input().split()))
    for j, value in enumerate(row):
        position[value] = (i, j)

costs = {i: 0 for i in range(1, D+1)}
for i in range(1, D+1):
    current = i + D
    while current <= H*W:
        costs[current] = costs[current-D] + abs(position[current][0] - position[current-D][0]) + abs(position[current][1] - position[current-D][1])
        current += D

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    MP = costs[R] - costs[L]
    print(MP)
