N = int(input())
A = sorted(list(map(int, input().split())))

a1 = A[-1]
med = (a1+1) // 2

B = [abs(a - med) for a in A]
idx = B.index(min(B))
a2 = A[idx]

print(a1, a2)
