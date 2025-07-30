#%%
T = int(input())

for t in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    answer = 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    x, y = (0, 0)
    d_x, d_y = directions[0]
    directions.append(directions.pop(0))

    for _ in range(N*N):
        arr[x][y] = answer
        answer += 1

        n_x, n_y = x + d_x, y + d_y

        if not (0 <= n_x < N and 0 <= n_y < N and arr[n_x][n_y] == 0):
            d_x, d_y = directions[0]
            directions.append(directions.pop(0))
            n_x, n_y = x + d_x, y + d_y
        
        x, y = n_x, n_y
    
    print(f'#{t+1}')
    for row in arr:
        print(' '.join(map(str, row)))
# %%
