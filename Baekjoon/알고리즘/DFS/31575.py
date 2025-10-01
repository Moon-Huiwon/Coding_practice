import sys
input = sys.stdin.readline

def dfs(row, col):
    global ans
    
    if ans == 'Yes':
        return

    if (row, col) == (M-1, N-1):
        ans = 'Yes'
        return

    visited[row][col] = 1
    for dx, dy in [(1,0),(0,1)]:
        nx, ny = row+dx, col+dy
        if 0 <= nx < M and 0 <= ny < N \
            and arr[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
ans = 'No'
visited = [[0]*N for _ in range(M)]
dfs(0,0)
print(ans)