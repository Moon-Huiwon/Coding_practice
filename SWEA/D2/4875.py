# DFS 활용한 코드
# Runtime error 발생 -> rstirp으로 인해 발생
def dfs(row, col):
    global ans
    
    # 현재 위치의 값이 3이면 stop
    if arr[row][col] == 3:
        ans = 1
        return
    
    # 방문 처리
    visited[row][col] = 1

    # 네방향으로 이동
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 조건에 맞는 방향으로 이동하고, 막히면 다시 돌아감
    for dx, dy in delta:
        nx, ny = row + dx, col + dy
        if 0 <= nx < N and 0 <= ny < N \
                and arr[nx][ny] in [0, 3] \
                and visited[nx][ny] == 0:
            
            dfs(nx, ny)
        
T = int(input())
for t in range(T):
    N = int(input())
    start_row = 0
    start_col = 0
    arr = []
    for i in range(N):
        tmp = list(map(int, input().rstrip()))
        if 2 in tmp:
            start_row = i
            start_col = tmp.index(2)
        
        arr.append(tmp)
    
    # 방문 처리하기 위한 초기 코드
    visited = [[0]*N for _ in range(N)]
    
    # 정답 도출
    ans = 0
    dfs(start_row, start_col)

    print(f'#{t+1} {ans}')


#%%
# stack을 활용한 코드
# Runtime error 발생 -> rstirp으로 인해 발생
T = int(input())
for t in range(T):
    N = int(input())
    start_row = 0
    start_col = 0
    arr = []
    for i in range(N):
        tmp = list(map(int, input().rstrip()))
        if 2 in tmp:
            start_row = i
            start_col = tmp.index(2)
        
        arr.append(tmp)
    
    # 방문 처리하기 위한 초기 설정
    visited = [[0]*N for _ in range(N)]
    
    # 갈 수 있지만 방문하지 않은 곳 stack에 저장
    stack = []
    stack.append((start_row, start_col))

    ans = 0
    while stack:
        # 현재 위치 받기
        cx, cy = stack.pop()
        # 방문 처리
        visited[cx][cy] = 1

        # 현재 위치 값이 3이면 멈춤(도착이기 때문)
        if arr[cx][cy] == 3:
            ans = 1
            break
        
        # 네방향으로 이동
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 네방향 살펴보고 갈 수 있으면 stack에 쌓기
        for dx, dy in delta:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N \
                    and arr[nx][ny] in [0, 3] \
                    and visited[nx][ny] == 0:
                
                stack.append((nx, ny))
        

    print(f'#{t+1} {ans}')