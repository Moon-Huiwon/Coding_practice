def bfs(start):
    # 출발 지점 저장
    q = []
    q.append(start)
   
   # 방문 처리
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1
   
   # 이동 가능한 방향
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        row, col = q.pop(0)
        # 종료 조건
        if arr[row][col] == 3:
            return  1
        
        for dx, dy in delta:
            nx, ny = row + dx, col + dy
            if 0 <= nx < N and 0 <= ny < N \
                and arr[nx][ny] != 1 \
                and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[row][col] + 1
        
    return 0

for _ in range(10):
    # 테스트 케이스
    tc = int(input())
    # 미로 크기
    N = 16
    # 미로
    arr = [list(map(int, input().rstrip())) for _ in range(N)]
    # 출발 지점 확인하기
    start_row = 0
    start_col = 0
    for i in range(N):
        if 2 in arr[i]:
            start_row = i
            start_col = arr[i].index(2)
            break
        
    # 정답 확인
    ans = bfs([start_row, start_col])
    print(f'#{tc} {ans}')
