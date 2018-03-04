H, W, D = map(int, input().split())
pos = [None]*(H*W)

for i in range(H):
    row = list(map(int, input().split()))
    for j in range(W):
        pos[row[j]-1] = (i, j)

costs = [0]*(H*W)
for i in range(1, D+1):
    current = i + D
    while current <= H*W:
        costs[current - 1] = costs[current - 1 - D] + abs(pos[current - 1][0] - pos[current - 1 - D][0]) + abs(pos[current - 1][1] - pos[current - 1 - D][1])
        current += D

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    MP = costs[R-1] - costs[L-1]
    print(MP)
