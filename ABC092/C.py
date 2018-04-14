N = int(input())
A = [0]
A += list(map(int, input().split()))
A += [0]

cost = [abs(A[i] - A[i+1]) for i in range(N+1)]
original_cost = sum(cost)

for i in range(N):
    ans = original_cost
    ans -= cost[i]
    ans -= cost[i+1]
    ans += abs(A[i] - A[i+2])

    print(ans)
