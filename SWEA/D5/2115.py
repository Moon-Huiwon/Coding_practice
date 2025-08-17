def dfs(cnt, quantity, sm, ci, cj):
    global max_quantity
    
    # quantity > C 이면 바로 종료
    if quantity > C:
        return
    
    # cnt == M 이면 max_quantity 업데이트하고 종료
    if cnt == M:
        max_quantity = max(max_quantity, sm)
        return
    
    # 핵심 포인트***
    # 부분집합 구하는 느낌 (OO/OX/XO/XX) 이걸 다 고려해서 max_quantity 업데이트
    # 해당 벌꿀 수집
    dfs(cnt+1, quantity+arr[ci][cj+cnt], sm+arr[ci][cj+cnt]**2, ci, cj)
    # 수집하지 않음
    dfs(cnt+1, quantity, sm, ci, cj)

T = int(input())
for t in range(T):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # ans와 sm 초기화
    ans = 0
    
    # memoization 활용
    # 각 위치에 max_quantity 저장하기
    memo = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N-(M-1)):
            max_quantity = 0
            dfs(0, 0, 0, i, j)
            memo[i][j] = max_quantity
    
    # 첫번째 일꾼 범위 (i1, j1)
    for i1 in range(N):
        for j1 in range(N-(M-1)):
            # 두번째 일꾼 범위 (i2, j2)
            for i2 in range(i1, N): # 두번째 일꾼은 첫번째 일꾼 범위 이후임
                # 첫번째 일꾼이랑 같은 행이면 j2 범위 설정이 j1+M 이어야함
                # 다른 행이면 0부터 가능
                sj = j1+M if i2 == i1 else 0 
                for j2 in range(sj, N-(M-1)):
                    ans = max(ans, memo[i1][j1] + memo[i2][j2])
    
    print(f'#{t+1} {ans}')
