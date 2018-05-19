# Typical DP: C

def prob_P_wins(R_p, R_q):
    return 1/(1 + 10**((R_q - R_p) / 400))

K = int(input())
R = []
for _ in range(2**K):
    R.append(int(input()))

dp = {i: {j: 0 for j in range(1, 2**i + 1)} for i in range(K+1)}

# TODO

print(*dp[K].values(), sep = '\n')
