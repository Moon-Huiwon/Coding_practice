# 처음시도 -> 시간초과
# 'W'가 아닌 'L'에서 출발해서 모든 이동 횟수 비교해서 최소값을 도출하는 방법
# 가지치기를 이용해도 시간 초과 발생

# 최종 코드
# 'W'에서 전부 상하좌우로 이동하여 가장 인접한 땅의 값 먼저 도출
from collections import deque

def bfs():
    global ans

    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append([i,j])
    
    while q:
        cx, cy = q.popleft()

        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in delta:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < M \
                and arr[nx][ny] == 'L' \
                    and visited[nx][ny] == 0:
                
                visited[nx][ny] = visited[cx][cy] + 1
                # 모든 이동 횟수를 구해야 하므로
                ans += visited[nx][ny]
                q.append([nx, ny])

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    ans = 0
    visited = [[0]*M for _ in range(N)]

    bfs()
    
    print(f'#{t+1} {ans}')


# 시간 조금 더 줄여주는 방법 (1초 더 빠름)
from collections import deque

def bfs():

    global ans
    
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append([i,j])
                visited[i][j] = 1
    
    while q:
        cx, cy = q.popleft()

        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in delta:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < M \
                    and visited[nx][ny] == 0:
                
                visited[nx][ny] = visited[cx][cy] + 1
                
                # 모든 이동 횟수를 구해야 하므로
                ans += visited[nx][ny] - 1
                q.append([nx, ny])

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    ans = 0
    visited = [[0]*M for _ in range(N)]

    bfs()
    
    print(f'#{t+1} {ans}')


#%%
import sys
sys.stdin = open("input.txt")
from collections import deque

def bfs():
    global ans
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < M \
                and visited[nx][ny] == 0 \
                    and arr[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                ans += visited[nx][ny]

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    ans = 0
    bfs()
    print(f'#{t+1} {ans}')