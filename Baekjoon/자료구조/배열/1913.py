#%%
N = int(input())
find_num = int(input())

matrix = [[0]*N for _ in range(N)]
distance = [(1, 0), (0, 1), (-1, 0), (0, -1)]

cx, cy = (0, 0)
init_num = N**2
matrix[cx][cy] = init_num

row = 0
col = 0
distance_idx = 0
while init_num > 1:
    dx, dy = distance[distance_idx % 4]
    
    if (0 <= cx + dx < N and 0 <= cy + dy < N and matrix[cx + dx][cy + dy] == 0):
        init_num -= 1
        cx, cy = cx + dx, cy + dy
        matrix[cx][cy] = init_num
        
        if init_num == find_num:
            row = cx
            col = cy
    else:
        distance_idx += 1

for i in range(N):
    print(*matrix[i])

print(row+1, col+1)

