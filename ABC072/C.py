N = int(input())
A = list(map(int, input().split()))

maximum = max(A)
count = [0]*(maximum + 2)

for i in range(N):
    if A[i] == 0:
        count[0] += 1
        count[1] += 1

    elif A[i] == maximum:
        count[A[i]] += 1
        count[A[i] - 1] += 1

    else:
        count[A[i] + 1] += 1
        count[A[i]] += 1
        count[A[i] - 1] += 1

print(max(count))
