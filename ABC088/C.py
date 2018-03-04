import numpy as np

C = []

for _ in range(3):
    C.append(list(map(int, input().split())))

C = np.array(C)

row = [np.unique(C[i,:] - C[i+1, :]).shape[0] for i in range(2)]
column = [np.unique(C[:,i] - C[:, i+1]).shape[0] for i in range(2)]

if sum(np.concatenate((row, column), axis = 0)) == 4:
    print("Yes")
else:
    print("No")
