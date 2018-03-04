import math

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_manipulation =  sum(B) - sum(A)

manipulation_A = 0
manipulation_B = 0

for i in range(N):
    if A[i] < B[i]:
        manipulation_A += math.ceil((B[i] - A[i]) / 2)
        manipulation_B += (B[i] - A[i]) % 2
    elif A[i] > B[i]:
        manipulation_B += A[i] - B[i]

if total_manipulation - max(manipulation_A, manipulation_B) >= 0:
    print("Yes")
else:
    print("No")
