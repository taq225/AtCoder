N = int(input())
P = list(map(int, input().split()))

dist = [P[i-1] - i for i in range(1, N+1)]

count = 0

for i in range(N):
    if dist[i] == 0:
        count += 1
        if i < N-1:
            dist[i] -= 1
            dist[i+1] += 1
        else: # i == N-1
            dist[i] += 1
            dist[i-1] -= 1

print(count)
