N = int(input())
X = list(map(int, input().split()))
Y = X[:]
Y = sorted(Y)

med1 = Y[N // 2 - 1]
med2 = Y[N // 2]

for x in X:
    if x < med2:
        print(med2)
    else:
        print(med1)
