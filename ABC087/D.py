from collections import deque

N, M = map(int, input().split())

X = [0 for _ in range(N+1)]
edges = [[] for _ in range(N+1)]

contradiction = False

# constructing a weighted digraph
for i in range(M):
    l, r, d = map(int, input().split())
    edges[l].append((r, d))
    edges[r].append((l, -d))

searched = set()
q = deque()

# assign x coordinate for each vertex with dfs
for i in range(N+1):
    if i in searched:
        continue
    q.append(i)
    searched.add(i)
    X[i] = 0
    while len(q) != 0:
        a = q.pop()
        for b, d in edges[a]:
            if b not in searched:
                q.append(b)
                searched.add(b)
                X[b] = X[a] + d
            else:
                if X[b] != X[a] + d: # verification
                    contradiction = True
                    print("No")
                    break
        if contradiction:
            break
    if contradiction:
        break
else:
    print("Yes")
