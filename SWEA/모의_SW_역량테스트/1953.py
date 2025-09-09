from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

types = {
    # 상하좌우
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0],
}

def bfs(R, C):
    q = deque([(R,C)])
    visited[R][C] = 1
    while q:
        cx, cy= q.popleft()
        dirs = types[arr[cx][cy]]
        for dir in range(4): # 상하좌우 확인
            # 출구가 없으면 다음 방향 확인
            if dirs[dir] == 0:
                continue

            nx = cx + dx[dir]
            ny = cy + dy[dir]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if arr[nx][ny] == 0:
                continue

            if visited[nx][ny] > 0:
                continue

            next_dirs = types[arr[nx][ny]]

            # 현재 상좌 -> next_dirs가 하우 가 안뚫렸으면 못간다
            if dir % 2 == 0 and next_dirs[dir + 1] == 0:
                continue
            # 현재 하우 -> next_dirs의 상좌가 안뚫렸으면 못간다
            if dir % 2 == 1 and next_dirs[dir - 1] == 0:
                continue

            if visited[cx][cy] + 1 > L:
                continue

            visited[nx][ny] = visited[cx][cy] + 1
            q.append((nx, ny))

T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    bfs(R, C)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1
    
    print(f'#{t+1} {cnt}')