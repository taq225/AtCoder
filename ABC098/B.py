N = int(input())
S = input()
maximum = 0

for i in range(1, N):
    S1 = set(S[:i])
    S2 = set(S[i:])
    count = len(S1 & S2)
    if maximum < count:
        maximum = count

print(maximum)
