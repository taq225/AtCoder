N, Y = map(int, input().split())

flag = False

for z in range(N + 1)[::-1]:
    rem1 = N - z + 1
    for y in range(rem1)[::-1]:
        x = N - z - y
        val = 10000*x + 5000*y + 1000*z
        if val == Y:
            flag = True
            break
    if flag:
        break

if not flag:
    x = -1
    y = -1
    z = -1

print(x, y, z)
