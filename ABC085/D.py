import math

N, H = map(int, input().split())
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

a_max = max(A)

B = sorted([x for x in B if x > a_max], reverse = True)

attack = 0

for damage in B:
    H -= damage
    attack += 1
    if H <= 0:
        break

if H > 0:
    attack += math.ceil(H / a_max)

print(attack)
