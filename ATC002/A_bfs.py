from collections import deque

R, C = map(int, input().split())
start_x, start_y = map(int, input().split())
goal_x, goal_y = map(int, input().split())

map_data = []

for i in range(R):
    string = input()
    map_data.append(string)

distance = {i: {j: None for j in range(C)} for i in range(R)}

def bfs(x, y):
    q = deque([]) # queue
    q.append(((x, y), 0))

    while len(q) != 0:
        (i, j), d = q.popleft()
        if i < 0 or i > R-1 or j < 0 or j > C-1:
            continue
        if distance[i][j] != None:
            continue
        if map_data[i][j] == '#':
            continue
        else:
            distance[i][j] = d
            q.append(((i+1, j), d+1))
            q.append(((i-1, j), d+1))
            q.append(((i, j+1), d+1))
            q.append(((i, j-1), d+1))
    return

bfs(start_x-1, start_y-1)

print(distance[goal_x-1][goal_y-1])
