def dfs(n, cx, cy, visitied):
    global ans
    
    # 가지치기: 절반을 돌았는데 *2 해도 ans보다 작거나 같다면 정답 갱신 불가
    # 시간 단축을 위해 사용하지만 사용하지 않아도 괜찮다.
    if n == 2 and ans >= len(visitied)*2:
        return
    
    if n > 3: # 방향을 바꾼 횟수는 최대 3번 이어야한다.
        return
    
    if n == 3 and (i,j) == (cx, cy): # 처음 출발 지점으로 오면 정답 도출
        ans = max(ans, len(visitied))
        return
    
    for k in range(n, n+2): # 방향은 총 2가지 가능 (기존 방향 유지 / 방향 변경)
        dx, dy = delta[n]
        nx, ny = cx + dx, cy + dy
        
        if 0 <= nx < N and 0 <= ny < N \
            and arr[nx][ny] not in visitied:
                visitied.append(arr[nx][ny])
                dfs(k, nx, ny, visitied)
                visitied.pop() # 백트래킹 작업 (탐색이 안된 곳으로 이동할 수 있도록)

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    delta = [(1,1), (1,-1), (-1,-1), (-1,1), (1,1)]
    for i in range(0, N-2):
        for j in range(1, N-1):
            dfs(0, i, j, [])
    
    print(f'#{t+1} {ans}')