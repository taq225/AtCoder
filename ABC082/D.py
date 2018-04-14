from collections import deque

def tpl_add(tpl1, tpl2):
    return tuple(tpl1[i] + tpl2[i] for i in range(len(tpl1)))

string = input()
x, y = map(int, input().split())

state = {
    0: (1, 0), # x_positive
    1: (0, 1), # y_positive
    2: (-1, 0), # x_negative
    3: (0, -1) # y_negative
}

current = state[0]

cand = [(0, 0)]

for s in string:
    if s == 'F':

    else:
        
