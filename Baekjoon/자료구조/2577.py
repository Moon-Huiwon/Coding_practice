#%%
num_cnt = [0] * 10

A = int(input())
B = int(input())
C = int(input())

number = A*B*C

for n in str(number):
    num_cnt[int(n)] += 1

for cnt in num_cnt:
    print(cnt)
# %%
