S = input()
flags = {'a': False, 'b': False, 'c': False}

for i in range(len(S)):
    flags[S[i]] = True

if flags['a'] and flags['b'] and flags['c']:
    print("Yes")
else:
    print("No")
