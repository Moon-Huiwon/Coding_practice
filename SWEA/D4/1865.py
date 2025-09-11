import sys
sys.stdin = open('input.txt')

def max_probability(row, value):
    global ans

    if value <= ans: # value에 곱해지는 값은 0보다 작은 값으로 곱할 수록 작아지기 때문에 value <= ans 로 가지치기 가능
        return

    if row == N: # 종료조건
        ans = max(ans, value)
        return

    for col in range(N):
        if visited[col] == 0 and arr[row][col] != 0: # 방문하지 않은 곳과 0이 아닌 곳으로 이동
            visited[col] = 1 # 방문처리
            max_probability(row+1, value*(arr[row][col]/100)) # value 값 업데이트
            visited[col] = 0 # 백트래킹을 위해 초기화

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    ans = 0
    max_probability(0, 1)
    print(f'#{t+1} {round(ans*100, 6):0.6f}')