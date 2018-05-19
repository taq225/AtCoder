lst = list(map(int, input().split()))
K = int(input())

lst = list(reversed(sorted(lst)))

print(lst[0]*2**K + sum(lst[1:]))
