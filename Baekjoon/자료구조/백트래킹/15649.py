import sys
input = sys.stdin.readline

def backtracking(n, lst):
    if n == M: # 종료 조건
        ans.append(lst)
        return

    for i in range(1, N+1): # 1~N까지 돌리기
        if visited[i] == 0: # 방문 안한 숫자만 방문할 것
            visited[i] = 1 # 방문 처리
            backtracking(n+1, lst + [i]) # 다음 숫자로 넘어가고 리스트에 저장
            visited[i] = 0 # 백트래킹 (종료된 후 방문 처리 다시 복구)

N, M = map(int, input().split())
visited = [0] * (N+1)
ans = []
backtracking(0,[])

for i in range(len(ans)):
    print(*ans[i])