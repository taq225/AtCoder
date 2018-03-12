N = int(input())
P = list(map(int, input().split()))

count = 0
for i in range(N):
    if i == P[i]-1:
        count += 1
        if i < N-1:
            P[i], P[i+1] = P[i+1], P[i]

print(count)
