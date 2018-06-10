N = int(input())

withdraw = N # 最大 N 回引き出すことになる.

for A in range(N+1):
    counter = 0
    temp = A
    while temp > 0: # Aを6進法で表した時の各桁の和が引き出した回数
        q, r = divmod(temp, 6)
        counter += r
        temp = q

    temp = N - A
    while temp > 0: # N-A を 9進法で表した時の各桁の和が引き出した回数
        q, r = divmod(temp, 9)
        counter += r
        temp = q

    if withdraw > counter:
        withdraw = counter

print(withdraw)
