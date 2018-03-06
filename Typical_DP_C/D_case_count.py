from collections import defaultdict

N, D = map(int, input().split())

# check whether D = 2^x * 3^y * 5^z or not
x, y, z = (0, 0, 0)
while D % 2 == 0:
    D //= 2
    x += 1
while D % 3 == 0:
    D //= 3
    y += 1
while D % 5 == 0:
    D //= 5
    z += 1
if D != 1:
    print(0)
    exit()

dp = defaultdict(int)
dp[(0,0,0)] = 1

for _ in range(N):
    check = list(dp.items())
    for pattern, count in check:
        p, q, r = pattern
        dp[(min(p+1, x), q, r)] += count # 2
        dp[(p, min(q+1, y), r)] += count # 3
        dp[(min(p+2, x), q, r)] += count # 4
        dp[(p, q, min(r+1, z))] += count # 5
        dp[(min(p+1, x), min(q+1, y), r)] += count # 6

print(dp[(x, y, z)]/(6**N))
