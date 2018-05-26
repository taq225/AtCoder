N = int(input())
A = list(map(int, input().split()))

r = 0
std_sum = 0 # standard summation
xor_sum = 0 # xor summation
count = 0

for l in range(N):
    while (r != N and std_sum + A[r] == xor_sum ^ A[r]):
        std_sum += A[r]
        xor_sum ^= A[r]
        r += 1

    count += r - l
    std_sum -= A[l]
    xor_sum ^= A[l]

print(count)
