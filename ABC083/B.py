N, a, b= map(int, input().split())
summation = 0

for i in range(N+1):
    num = i
    total = 0
    while num != 0:
        q, mod = divmod(num, 10)
        total += mod
        num = q

    if total >= a and total <= b:
        summation += i

print(summation)
