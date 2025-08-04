#%%
num = int(input())

paper = [[0] * 100 for _ in range(100)]

for _ in range(num):
    x, y = map(int, input().split())
    for i in range(x-1, x+10-1):
        for j in range(y-1, y+10-1):
            paper[i][j] = 1

answer = 0
for i in range(100):
    answer += sum(paper[i])

print(answer)
# %%
