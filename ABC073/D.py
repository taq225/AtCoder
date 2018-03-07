import itertools
from collections import defaultdict
from heapq import heappush, heappop

inf = float("inf")

N, M, R = map(int, input().split())
towns = list(map(int, input().split()))

vertices = [i for i in range(1, N+1)]
edge_costs = {i: defaultdict(int) for i in range(N+1)}

for _ in range(M):
    a, b, c = map(int, input().split())
    edge_costs[a][b] = c
    edge_costs[b][a] = c

def dijkstra(s):
    dist = [inf for _ in range(N+1)]
    dist[s] = 0
    searched = [False for _ in range(N+1)]

    q = [] # heap
    heappush(q, (0, s))

    while len(q) != 0:
        d, v = heappop(q)
        # don't need to check when the stored vertex has been already searched,
        # or the stored value is greater than provisional distance
        if searched[v] or d > dist[v]:
            continue

        for u, c in edge_costs[v].items():
            temp = d + c
            if temp < dist[u]:
                dist[u] = temp
                heappush(q, (dist[u], u))

        searched[v] = True

        if sum(searched) == N: # finish when all vertices have been searched
            break

    return [dist[t] for t in towns]

D = [dijkstra(t) for t in towns]

ans = min([sum([D[perm[i]][perm[i+1]] for i in range(R-1)]) for perm in itertools.permutations(range(R))])
print(ans)
