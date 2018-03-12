A, B = map(int, input().split())
cand = [i*(10**4) + j*(10**3) + k*(10**2) + j*10 + i for i in range(1, 10) for j in range(0, 10) for k in range(0, 10)]

count = 0
for c in cand:
    if c >= A and c <= B:
        count += 1

print(count)
