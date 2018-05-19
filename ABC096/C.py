H, W = map(int, input().split())
grid = [input() for _ in range(H)]

paintable = True

for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            if i != 0:
                if grid[i-1][j] == '#':
                    continue
            if i != H - 1:
                if grid[i+1][j] == '#':
                    continue
            if j != 0:
                if grid[i][j-1] == '#':
                    continue
            if j != W - 1:
                if grid[i][j+1] == '#':
                    continue
            paintable = False
    if not paintable:
        break

print("Yes" if paintable else "No")
