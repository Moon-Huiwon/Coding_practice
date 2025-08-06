#%%
# import sys
# sys.stdin = open("input.txt")
# 최종 답안
from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

init_check = [[0]*N for _ in range(M)]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

answer = 0

for i in range(M):
    for j in range(N):
        if init_check[i][j] == 0 and arr[i][j] == 1:
            q = deque()
            q.append((i,j))
            init_check[i][j] = 1 # 큐에 넣을 때 방문 처리***

            while q:
                x, y = q.popleft()
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < M and 0 <= ny < N \
                        and init_check[nx][ny] == 0 \
                            and arr[nx][ny] == 1:
                        q.append((nx, ny))
                        init_check[nx][ny] = 1 # 방문 체크는 여기서(큐에 넣을 때)***
            
            answer += 1
        else:
            init_check[i][j] = 1

print(answer)

#%%
# 원본 코드 (시간 초과)
"""
원인1: deque 사용X -> 리스트에서 pop하는 경우 시간이 오래 걸림
원인2: init_check의 위치가 부적절함 -> 큐에 넣을 때 바로 처리할 수 있도록 설정 (중복 삽입 방지)
"""
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

init_check = [[0]*N for _ in range(M)]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

q = []
answer = 0
for i in range(M):
    for j in range(N):
        if init_check[i][j] == 0 and arr[i][j] == 1:
            q.append([i,j])
        
            while q:
                # print(q)
                x, y = q.pop(0)
                init_check[x][y] = 1
            
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < M and 0 <= ny < N \
                        and init_check[nx][ny] == 0 \
                            and arr[nx][ny] == 1:
                        q.append([nx, ny])
            
            answer += 1
            

        else:
            init_check[i][j] = 1

print(answer)