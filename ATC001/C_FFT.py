# TODO

from collections import defaultdict

N = int(input())
A = defaultdict(int)
B = defaultdict(int)
for i in range(N):
    A[i], B[i] = map(int, input().split())
