import sys
sys.stdin = open('input.txt')

def sum_value(row, value):
    global ans

    if value >= ans: # 가지치기
        return
    
    if row == N: # 종료조건
        ans = min(ans, value) # 정답 업데이트
        return
    
    for j in range(N):
        if visited[j] == 0: # 방문하지 않았을 때
            visited[j] = 1 # 방문표시
            sum_value(row+1, value + arr[row][j]) # 다음 행으로 이동 / value 값 업데이트
            visited[j] = 0 # 백트래킹을 위해 초기화

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = float('inf')
    sum_value(0, 0)
    print(f'#{t+1} {ans}')