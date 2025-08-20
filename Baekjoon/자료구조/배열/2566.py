#%%
matrix = []
for _ in range(9):
    matrix.append(list(map(int, input().split())))

row = 0
col = 0
max_value = 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            row = i
            col = j

print(max_value)
print(row+1, col+1)
