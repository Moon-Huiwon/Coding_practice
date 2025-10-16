import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

from collections import deque

def bfs(row, col):
    global cnt
    q = deque([[row, col]])
    visited[row][col] = 1
    while q:
        cx, cy = q.popleft()
        cnt += 1
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < M and 0 <= ny < N \
                and arr[nx][ny] == 0 \
                    and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
    


M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1, x1 + (x2-x1)):
        for y in range(y1, y1 + (y2-y1)):
            arr[x][y] = 1

visited = [[0]*N for _ in range(M)]

ans = []
for i in range(M):
    for j in range(N):
        cnt = 0
        if visited[i][j] == 0 and arr[i][j] == 0:
            bfs(i, j)
        
        if cnt > 0:
            ans.append(cnt)

ans.sort()
print(len(ans))
print(*ans)