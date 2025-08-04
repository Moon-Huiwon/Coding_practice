#%%
N, M = map(int, input().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(N):
    value_list = list(map(int, input().split()))
    for j in range(M):
        matrix[i][j] += value_list[j]

for i in range(N):
    print(*matrix[i])

# %%
