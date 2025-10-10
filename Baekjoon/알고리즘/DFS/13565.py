import sys
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(row, col):
    global ans
    if row == M-1:
        ans = 'YES'
        return
    
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = row+dx, col+dy
        if 0 <= nx < M and 0 <= ny < N \
            and arr[nx][ny] == '0' \
                and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny)

M, N = map(int, input().split())
arr = list(list(input()) for _ in range(M))
visited = [[0]*N for _ in range(M)]

ans = 'NO'

for idx in range(N):
    if visited[0][idx] == 1 or arr[0][idx] == '1':
        continue
    
    visited[0][idx] = 1
    dfs(0, idx)

print(ans)