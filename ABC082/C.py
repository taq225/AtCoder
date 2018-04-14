import collections

N = int(input())
A = list(map(int, input().split()))

count = collections.Counter()

for a in A:
    count[a] += 1

ans = 0

for num, c in count.items():
    if num < c:
        ans += c - num
    elif num > c:
        ans += c
    else:
        continue

print(ans)
