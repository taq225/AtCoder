H, W = map(int, input().split())
lst = []
for _ in range(H):
    lst.append(input())

A = []
whites = 0

for i in range(H):
    row_i = []
    for j in range(W):
        if lst[i][j] == '.':
            whites += 1
            tmp = []
            if i != 0:
                if lst[i-1][j] == '.':
                    tmp.append((i-1, j))
            if j != 0:
                if lst[i][j-1] == '.':
                    tmp.append((i, j-1))
            if i != H-1:
                if lst[i+1][j] == '.':
                    tmp.append((i+1, j))
            if j != W-1:
                if lst[i][j+1] == '.':
                    tmp.append((i, j+1))
            row_i.append(tmp)
        else:
            row_i.append([])
    A.append(row_i)

Q = [(0, 0, 0)]
visited = []

flag = False

while len(Q) != 0:
    x, y, path_length = Q.pop(0)
    if (x,y) == (H-1, W-1):
        flag = True
        break
    if (x,y) not in visited:
        visited.append((x,y))
        Q += [(i, j, path_length + 1) for (i, j) in A[x][y]]

if flag:
    print(whites - path_length - 1)
else:
    print(-1)
