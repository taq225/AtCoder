A = int(input())
B = int(input())
C = int(input())
X = int(input())

cand = [(i, j, k) for i in range(A+1) for j in range(B+1) for k in range(C+1)]
count = 0

for c in cand:
    if 500*c[0] + 100*c[1] + 50*c[2] == X:
        count += 1

print(count)
