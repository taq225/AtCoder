import collections

N = int(input())
S = []
for _ in range(N):
    S.append(input())
M = int(input())
T = []
for _ in range(M):
    T.append(input())

count = collections.Counter()

for s in S:
    count[s] += 1
for t in T:
    count[t] -= 1

print(max(count.most_common(1)[0][1], 0))
