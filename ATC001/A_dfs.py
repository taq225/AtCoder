from collections import deque

H, W = map(int, input().split())
state = []
for i in range(H):
    string = input()
    state.append(string)
    j = string.find('s')
    if j != -1:
        start = (i, j)

searched = {i: {j: False for j in range(W)} for i in range(H)}

def dfs(x, y):
    q = deque([]) # stack
    q.append((x,y))

    while len(q) != 0:
        i, j = q.pop()
        if i < 0 or i > H-1 or j < 0 or j > W-1:
            continue
        if searched[i][j]:
            continue
        if state[i][j] == '#':
            continue
        if state[i][j] == 'g':
            return True
        q.append((i+1, j))
        q.append((i-1, j))
        q.append((i, j+1))
        q.append((i, j-1))
        searched[i][j] = True
    return False

if dfs(*start):
    print("Yes")
else:
    print("No")
