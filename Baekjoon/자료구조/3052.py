#%%
remain_list = []
for _ in range(10):
    num = int(input())
    remain_list.append(num % 42)

print(len(set(remain_list)))