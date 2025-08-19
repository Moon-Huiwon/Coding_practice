T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(M):

            current_cnt = 0
            current_cnt += arr[i][j]
            delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in delta:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M:
                    current_cnt += arr[nx][ny]
            
            ans = max(ans, current_cnt)
    
    print(f'#{t+1} {ans}')
