N = int(input())
A = input().split()
A = list(map(int, A))

A.sort()
A.reverse()

Alice = sum(A[0::2])
Bob = sum(A[1::2])

print(Alice - Bob)
