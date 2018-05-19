import itertools

N = int(input())
table = [input() for _ in range(N)]

count = 0

for b in range(N):
    symmetric = True
    new_table = []
    for i in range(N):
        string = table[i][b:] + table[i][:b]
        new_table.append(string)

    for i in range(N-1):
        string1 = new_table[i][i+1:]
        string2 = ''.join([s[i] for s in new_table[i+1:]])
        if string1 != string2:
            symmetric = False
            break

    if symmetric:
        count += N

print(count)
