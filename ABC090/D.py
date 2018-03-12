N, K = map(int, input().split())

count = 0

for b in range(K+1, N+1): # K <= remainder < b (divisor) <= N
    q_max = N // b
    count += q_max * (b - K) # a = q*b + r (q = 0, ..., q_max; r = K, ..., b-1)

    rem = N % b - K + 1
    if rem > 0:
        count += rem # a = q_max*b + r (r = K, ..., N%b)
        
    if K == 0:
        count -= 1 # eliminate the following case: 0 = 0*b + 0.

print(count)
