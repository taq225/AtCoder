n = int(input())
W = list(map(int, input().split()))

# O(n^3) time. TLE (n: up to 100).

# import sys
# sys.setrecursionlimit(150000)
#
# class Memoize:
#     def __init__(self, f):
#         self.f = f
#         self.cache = {}
#     def __call__(self, *args):
#         if args not in self.cache:
#             self.cache[args] = self.f(*args)
#         return self.cache[args]
#
# @Memoize
# def cost(i, j): # i <= j
#     if i == j:
#         return 0
#     else:
#         return min([cost(i, k) + cost(k+1, j) for k in range(i, j)]) + sum(W[i : j+1])
#
# print(cost(0, n-1))

# O(n^2) time. TLE (n: up to 100).

def cumsum(lst):
    sum_list = [0]
    for i in range(len(lst)):
        sum_list.append(sum_list[i] + lst[i])
    return sum_list

cumsum_W = cumsum(W)

cost = {i: {j: None for j in range(i, n+1)} for i in range(1, n+1)}
pos = {i: {j: None for j in range(i, n+1)} for i in range(1, n+1)}

for i in range(1, n+1):
    cost[i][i] = 0
    pos[i][i] = i

for i in range(1, n):
    cost[i][i+1] = cumsum_W[i+1] - cumsum_W[i-1]
    pos[i][i+1] = i

for l in range(2, n):
    for i in range(1, n-l+1):
        summation = cumsum_W[i+l] - cumsum_W[i-1]
        k0, k1 = pos[i][i+l-1], pos[i+1][i+l]
        min_c, min_idx = min([(cost[i][k] + cost[k+1][i+l], k) for k in range(k0, k1 + 1)])
        cost[i][i+l] = min_c + summation
        pos[i][i+l] = min_idx

print(cost[1][n])
