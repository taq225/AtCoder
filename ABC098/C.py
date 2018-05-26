N = int(input())
S = input()

# i番目の人の左にある E, W の数
count_E = [0]
count_W = [0]

for s in S:
    if s == 'E':
        count_E.append(count_E[-1] + 1)
        count_W.append(count_W[-1])
    else:
        count_E.append(count_E[-1])
        count_W.append(count_W[-1] + 1)

ans = 10**6

for i in range(N):
    rotate_left = count_W[i]
    rotate_right = count_E[-1] - count_E[i+1]
    total = rotate_left + rotate_right
    if total < ans:
        ans = total

print(ans)
