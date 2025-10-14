from collections import deque
import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

def bfs(row, col):
    q = deque([[row, col]])
    visited[row][col] = 1

    while q:
        cx, cy = q.popleft()
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < N and 0 <= ny < M \
                and visited[nx][ny] == 0 \
                    and arr[nx][ny] == '1':
                visited[nx][ny] = visited[cx][cy] + 1
                q.append([nx, ny])
            
            if (nx, ny) == (N-1, M-1) and visited[nx][ny] != 0:
                visited[nx][ny] = min(visited[nx][ny], visited[cx][cy]+1)



N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

bfs(0,0)
print(visited[N-1][M-1])