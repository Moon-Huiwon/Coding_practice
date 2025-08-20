#%%
basic_num = [1, 1, 2, 2, 2, 8]

white_num = list(map(int, input().split()))

answer = []
for i in range(len(basic_num)):
    answer.append(basic_num[i] - white_num[i])

print(*answer)