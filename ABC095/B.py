N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]

remainder = X - sum(M)
print(N + remainder // min(M))
