x, y= map(int, input().split())

lst = []

num = x

while num <= y:
    lst.append(num)
    num = 2*num

print(len(lst))
