N, M, X = map(int, input().split())
A = list(map(int, input().split()))

to_zero = 0
to_N = 0

for a in A:
    if a < X:
        to_zero += 1
    elif a > X:
        to_N += 1

print(min(to_zero, to_N))
