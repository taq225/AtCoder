num = list(map(int, input().split()))

maximum = max(num)
dif = [maximum - n for n in num]

counter = 0
odd = 0
for d in dif:
    q, r = divmod(d, 2)
    counter += q
    odd += r

if odd == 0:
    pass
elif odd == 1:
    counter += 2
else:
    counter += 1

print(counter)
