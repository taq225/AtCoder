from collections import defaultdict

N = int(input())
A = defaultdict(int)

for _ in range(N):
    a = int(input())
    if A[a] == 1:
        A[a] = 0
    else:
        A[a] = 1

print(sum(A.values()))
