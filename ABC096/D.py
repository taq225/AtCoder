import itertools
import math


def get_primes(x):
    if x < 2:
        return []

    primes = [i for i in range(x)]
    primes[1] = 0

    for prime in primes:
        if prime > math.sqrt(x):
            break
        if prime == 0:
            continue
        for non_prime in range(2 * prime, x, prime):
            primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]


N = int(input())
primes = get_primes(55555)
ans = []
i = 4

while len(ans) < N:
    p = primes[i]

    if p % 5 == 1:
        ans.append(p)

    i += 1

print(*ans)
