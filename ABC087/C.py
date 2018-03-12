def cumsum(lst):
    sum_list = [0]
    for i in range(len(lst)):
        sum_list.append(sum_list[i] + lst[i])
    return sum_list

N = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row2.reverse()

candy_cand1 = cumsum(row1)[1:]
candy_cand2 = cumsum(row2)[1:]
candy_cand2.reverse()

cand = [0]*N
for i in range(N):
    cand[i] = candy_cand1[i] + candy_cand2[i]

print(max(cand))
