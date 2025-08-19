T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(M):

            if arr[i][j] == 0:
                continue

            delta = [(0, 1), (1, 0)]
            for dx, dy in delta:
                current_value = 1
                nx, ny = i + dx, j + dy
                while 0 <= nx < N and 0 <= ny < M \
                    and arr[nx][ny] == 1:
                    current_value += 1
                    nx += dx
                    ny += dy
            
                ans = max(ans, current_value)
    
    print(f'#{t+1} {ans}')
