N = int(input())
C = []
S = []
F = []

for i in range(N-1):
    c, s, f= map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(N-1):
    time = 0
    for j in range(i, N-1):
        if time < S[j]:
            time = S[j]
        else:
            if time % F[j] != 0:
                time += F[j] - (time % F[j])
        time += C[j]
    print(time)

print(0)
