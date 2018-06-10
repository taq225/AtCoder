import itertools

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
grid = [list(map(int, input().split())) for _ in range(N)]

ans = 10**10

# (i+j)%3 で決まるグループ g に色 c のグリッドが何個あるかを計算
group = {g: {c: 0 for c in range(C)} for g in range(3)}
for i, row in enumerate(grid):
    for j, r in enumerate(row):
        group[(i+j)%3][r-1] += 1

for tup in itertools.combinations(range(C), 3):
    for c1, c2, c3 in itertools.permutations(tup):
        temp = 0 # 各グループを色 c1, c2, c3 で塗ったときの違和感の和が入る
        for c in range(C):
            for g, col in zip(range(3), [c1, c2, c3]):
                temp += group[g][c] * D[c][col]
        if ans > temp:
            ans = temp

print(ans)
