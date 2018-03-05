N = int(input())
P = list(map(int, input().split()))

possible = set([0])

for i in range(N): # consider problem 0 to problem i
    addition = set([j + P[i] for j in possible]) # possible points one will obtain if he/she can answer problem i
    possible |= addition

print(len(possible))
