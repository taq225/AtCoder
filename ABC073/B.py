N = int(input())
audience = []
for _ in range(N):
    l, r = map(int, input().split())
    audience.append(r - l + 1)

print(sum(audience))    
