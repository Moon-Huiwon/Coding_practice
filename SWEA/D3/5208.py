def backtracking(cnt, current):
    global ans

    if cnt >= ans: # 가지치기
        return
    
    if current >= N: # 정답 도출하기
        ans = min(ans, cnt)
        return
    
    max_value = min(N, current + charge_lst[current-1]) # 갈 수 있는 최대 위치 확인
    for i in range(current+1, max_value+1): # 다음으로 갈 수 있는 위치 범위
        backtracking(cnt+1, i) # cnt+1 해주고 다음위치로 이동

T = int(input())
for t in range(T):
    lst = list(map(int, input().split()))
    N = lst[0]
    charge_lst = lst[1:]
    ans = float('inf')
    backtracking(0, 1)
    print(f'#{t+1} {ans-1}')
    