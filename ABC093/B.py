A, B, K = map(int, input().split())

ans = []

if B - A + 1 > 2*K:
    ans += list(range(A, A + K))
    ans += list(range(B - K + 1, B + 1))

else:
    ans = list(range(A, B+1))

print(*ans, sep = "\n")
