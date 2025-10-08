import sys
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    global cnt, dimensions
    
    if arr[x][y] == 1:
        visited[x][y] = 1
        dimensions += 1
    
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x+dx, y+dy
        
        if 0<= nx < n and 0 <= ny < m \
            and arr[nx][ny] == 1 \
                and visited[nx][ny] == 0:
                    dfs(nx, ny)
            
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
cnt = 0
max_dimension = 0
for i in range(n):
    for j in range(m):
        dimensions = 0
        if arr[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            max_dimension = max(max_dimension, dimensions)
            cnt += 1

print(cnt)
print(max_dimension)