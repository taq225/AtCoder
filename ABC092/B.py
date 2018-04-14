N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in range(N):
    if D % A[i] == 0:
        X += D // A[i]
    else:
        X += D // A[i] + 1

print(X)
