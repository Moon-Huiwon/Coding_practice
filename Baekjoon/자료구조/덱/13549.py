# 메모리 초과 발생
# 이미 지나간 위치를 중복으로 들어가면서 메모리 초과 발생
# visited 활용하여 중복 제거하기
# K의 최대값을 넘어갈 수 없으므로 범위 설정할 것
import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())

def bfs(N, K, sec):
    q = deque()
    q.append([N, sec])

    while q:
        current_x, current_sec = q.popleft()

        if current_x == K:
            return current_sec
        
        if current_x > K:
            continue

        move_list = [current_x, -1, +1]
        for d in move_list:
            if abs(d) == 1:
                q.append([current_x+d, current_sec+1])    
            else:
                q.append([current_x+d, current_sec])
       
print(bfs(N, K, 0))

# 정답 코드
import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
max_value = 100001 # 최대 범위
visited = [0] * max_value # visited 생성

def bfs():
    q = deque()
    q.append((N, 0))

    while q:
        current_x, current_sec = q.popleft()

        if current_x == K:
            return current_sec
        
        # 순간 이동 범위 설정
        if 0 <= 2*current_x < max_value \
            and visited[2*current_x] == 0:
            visited[2*current_x] = 1 # 방문 처리
            q.appendleft((2*current_x, current_sec)) # 먼저 탐색할 수 있도로 appendleft() 사용
        
        # 이동 범위 설정
        for nx in [-1, 1]:
            if 0 <= current_x + nx < max_value \
                and visited[current_x + nx] == 0:
                visited[current_x + nx] = 1 # 방문 처리
                # 나중에 탐색할 수 있도록 append() 사용
                # 1초 지나야 하므로 cuurent_sec+1
                q.append((current_x + nx, current_sec+1))
        
print(bfs())