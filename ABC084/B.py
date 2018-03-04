a, b= map(int, input().split())
string = input()

flag = 1

for i in range(a):
    if string[i] == '-':
        flag = 0

if string[a] != '-':
    flag = 0

for i in range(a+1,a+b+1):
    if string[i] == '-':
        flag = 0

if flag == 1:
    print("Yes")

else:
    print("No")
