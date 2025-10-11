import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(x, y, length):
    global ans
    
    if length > K:
        return
    
    if length == K and (x, y) == (0, C-1):
        ans += 1
        return
    
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C \
            and arr[nx][ny] == '.' \
                and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dfs(nx, ny, length+1)
                    visited[nx][ny] = 0
                    
R, C, K = map(int, input().split())
arr = list(list(input()) for _ in range(R))
visited = [[0]*C for _ in range(R)]
visited[R-1][0] = 1
ans = 0
dfs(R-1, 0, 1)
print(ans)