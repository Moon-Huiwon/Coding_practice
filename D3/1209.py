
for _ in range(10):
    T = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    row_list = []
    for i in range(100):
        row_list.append(sum(arr[i]))

    row_num = max(row_list)

    col_list = []
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[j][i]
        col_list.append(tmp)

    col_num = max(col_list)

    right_x = 0
    dx, dy = (1,1)
    x, y = (0, 0)

    for _ in range(100):
        right_x += arr[x][y]
        
        x, y = x+dx, y+dy


    left_x = 0
    dx, dy = (1,-1)
    x, y = (0, 99)

    for _ in range(100):
        left_x += arr[x][y]
        
        x, y = x+dx, y+dy

    print(f'#{T} {max(row_num, col_num, right_x, left_x)}')