N_A, N_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp[i][j]: the maximum point first player will obtain when i objects are left in A and j objects in B
dp = {i: {j: 0 for j in range(N_B+1)} for i in range(N_A+1)}

for i in range(1, N_A+1):
    if ((N_A + N_B) - i) % 2 == 0: # first player
        dp[i][0] = dp[i-1][0] + A[N_A - i]
    else: # second player
        dp[i][0] = dp[i-1][0]

for j in range(1, N_B+1):
    if ((N_A + N_B) - j) % 2 == 0: # first player
        dp[0][j] = dp[0][j-1] + B[N_B - j]
    else: # second player
        dp[0][j] = dp[0][j-1]

for i in range(1, N_A+1):
    for j in range(1, N_B+1):
        if ((N_A + N_B) - (i + j)) % 2 == 0: # first player
            dp[i][j] = max(dp[i-1][j] + A[N_A - i], dp[i][j-1] + B[N_B - j])
        else: # second player
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])

print(dp[N_A][N_B])
