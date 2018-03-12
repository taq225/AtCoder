N, M, P = map(int, input().split())

def pow_mod(n, k, m):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return (pow_mod(n, k//2, m)**2) % m
    else:
        return (n * pow_mod(n, k-1, m)) % m

print(pow_mod(N, P, M))
