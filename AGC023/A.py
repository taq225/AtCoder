import collections


def binomial(n, k):
    if 0 <= k <= n:
        numer = 1
        denom = 1
        for t in range(1, min(k, n - k) + 1):
            numer *= n
            denom *= t
            n -= 1
        return numer // denom
    else:
        return 0


N = int(input())
A = list(map(int, input().split()))

cumsum = [0]
for a in A:
    cumsum.append(a + cumsum[-1])

count = collections.defaultdict(int)
for c in cumsum:
    count[c] += 1

ans = 0

for c in count.values():
    if c >= 2:
        ans += binomial(c, 2)

print(ans)
