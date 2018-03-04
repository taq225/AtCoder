import itertools

N = int(input())
S = []

for _ in range(N):
    S.append(input()[0])

num = [S.count(char) for char in ['M', 'A', 'R', 'C', 'H']]

if num.count(0) >= 3:
    print(0)
else:
    nonzero = [n for n in num if n != 0]
    case = list(itertools.combinations(nonzero, 3))
    total = sum([tpl[0]*tpl[1]*tpl[2] for tpl in case])

    print(total)
