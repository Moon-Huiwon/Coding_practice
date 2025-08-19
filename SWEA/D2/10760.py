T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(M):

            

            delta = [(1, 0), (1, -1), (1, 1), (0, -1), 
                     (0, 1), (-1, 0), (-1, -1), (-1, 1)]
            
            possible_cnt = 0
            for dx, dy in delta:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M \
                    and arr[nx][ny] < arr[i][j]:
                    possible_cnt += 1
            
            if possible_cnt >= 4:
                ans += 1
    
    print(f'#{t+1} {ans}')
                    
