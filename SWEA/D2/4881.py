def dfs(row, current_sum):
    # 정답 도출
    global ans
    
    # 가지치기: 최소값을 구하는 것이므로 중지
    if current_sum >= ans:
        return
    
    # row은 0~N-1까지 가능하기 때문에
    # row == N이면 중지하고, 정답 도출
    if row == N:
        ans = min(ans, current_sum)
        return

    # row는 하나씩 늘어가지만 col은 선택할 수 있는 경우의 수가 여러개 존재
    # ex) [0,0] - > [1, 1] or [1, 2]
    # 따라서 for문을 활용하여 여러가지 선택지 확인
    for col in range(N):
        if visitied[col] == 0:
            visitied[col] = 1
            dfs(row+1, current_sum + arr[row][col])
            visitied[col] = 0 # 백트래킹을 위한 코드
            
T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    visitied = [0] * N
    dfs(0, 0)

    print(f'#{t+1} {ans}')
    
