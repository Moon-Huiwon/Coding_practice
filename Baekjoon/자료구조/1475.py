#%%
num_cnt = [0]*9

N = input()
for n in N:
    if int(n) == 9:
        num_cnt[6] += 1
    else:
        num_cnt[int(n)] += 1

num_cnt[6] = num_cnt[6] // 2 + num_cnt[6] % 2

print(max(num_cnt))
# %%
