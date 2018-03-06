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

dp = [defaultdict(int) for _ in range(N+1)]
dp[0][(0,0,0)] = 1

for i in range(N):
    check = list(dp[i].items())
    for pattern, prob in check:
        p, q, r = pattern
        dp[i+1][(p, q, r)] += prob/6 #1
        dp[i+1][(min(p+1, x), q, r)] += prob/6 # 2
        dp[i+1][(p, min(q+1, y), r)] += prob/6 # 3
        dp[i+1][(min(p+2, x), q, r)] += prob/6 # 4
        dp[i+1][(p, q, min(r+1, z))] += prob/6 # 5
        dp[i+1][(min(p+1, x), min(q+1, y), r)] += prob/6 # 6

print(dp[N][(x, y, z)])
