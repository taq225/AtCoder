N = int(input())
D = []

for i in range(N):
    d = int(input())
    D.append(d)

length = len(list(set(D)))

print(length)
