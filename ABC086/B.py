import math

a, b = input().split()
n = int(a+b)

m = int(math.sqrt(n)**2)

if abs(m**2 - n) < 1e-6:
    print("Yes")
else:
    print("No")
