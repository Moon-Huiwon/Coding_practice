def backtracking(x, y, value):
    global ans

    # 가지치기 중요*** (작성안할 시 시간 초과)
    if value >= ans:
        return

    if x == N-1 and y == N-1:
        ans = min(ans, value)
        return

    for dx, dy in [(0,1), (1,0)]: # 오른쪽 / 아래 이동
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N \
            and visited[nx][ny] == 0:
            visited[nx][ny] = 1 # 방문 처리
            backtracking(nx, ny, value+arr[nx][ny]) # 다음 위치로 이동하여 확인
            visited[nx][ny] = 0 # 백트래킹

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 숫자 판 생성
    visited = [[0]*N for _ in range(N)] # 방문 여부 처리
    ans = float("inf")
    visited[0][0] = 1 # 맨 왼쪽 위 방문 처리 (시작점)
    backtracking(0, 0, arr[0][0]) # 함수 작동
    print(f'#{t+1} {ans}') # 결과 출력
