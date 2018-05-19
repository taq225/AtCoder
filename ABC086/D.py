# TODO: WIP

N, K = map(int, input().split())
X = []
Y = []
C = []

for _ in range(N):
    x, y, c = input().split()
    X.append(x)
    Y.append(y)
    C.append(c)

X = list(map(int, X))
Y = list(map(int, Y))

current_best = 0

for i in range(K):
    for j in range(K):
        val1 = 0
        val2 = 0

        temp_X = [(x - i) // K for x in X]
        temp_Y = [(y - j) // K for y in Y]
        flt = [(temp_X[idx] + temp_Y[idx]) % 2 for idx in range(N)]
        color = ['B' for _ in range(N)]

        if 1 in flt:
            color[flt.index(1)] = 'W'

        for idx in range(N):
            if C[idx] == color[idx]:
                val1 += 1
            else:
                val2 += 1

        val = max([val1, val2])

        if current_best < val:
            current_best = val

print(current_best)
