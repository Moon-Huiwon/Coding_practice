def backtracking(row, value, cnt):
    global ans
    
    if value >= ans: # 가지치기
        return

    if cnt == N-1: # 종료조건
        ans = min(ans, value+arr[row][0]) # 마지막 관리구역 더해주기
        return
    
    for i in range(N):
        if row != i and visited[i] == 0:
            visited[i] = 1 # 방문처리
            backtracking(i, value+arr[row][i], cnt+1)
            visited[i] = 0 # 백트래킹
        
T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N)
    ans = float("inf")
    visited[0] = 1 # 첫번째 구역은 마지막에 돌아갈 때만 이용해야하기 때문에 방문 처리
    backtracking(0,0,0)
    print(f'#{t+1} {ans}')