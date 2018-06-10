a, b = map(int, input().split())

dif = b - a

height_west = dif * (dif - 1) // 2

thickness = height_west - a

print(thickness)
