N = int(input())
T = []
X = []
Y = []

for _ in range(N):
    t, x, y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

current_t = 0
current_x = 0
current_y = 0

flag = True

for i in range(N):
    dist = (X[i] - current_x) + (Y[i] - current_y)
    time = T[i] - current_t
    if dist > time:
        flag = False
        break
    elif (time - dist)%2 != 0:
        flag = False
        break
    else:
        current_t = T[i]
        current_x = X[i]
        current_y = Y[i]

if flag == True:
    print("Yes")
else:
    print("No")
