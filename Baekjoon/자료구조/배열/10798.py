#%%
matrix = []
for _ in range(5):
    matrix.append(list(input()))

for j in range(15):
    for i in range(5):
        if len(matrix[i]) > j:
            print(matrix[i][j], end='')

