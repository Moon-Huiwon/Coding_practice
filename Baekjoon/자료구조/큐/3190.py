# import sys
# sys.stdin = open("input.txt")

N = int(input()) # 보드의 크기
K = int(input()) # 사과 개수
arr = [[0] * N for _ in range(N)] # 보드를 만들고 사과 위치에 1 저장
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

L = int(input()) # 방향 전환 정보 개수
snake_info = [] # 방향 전환 정보 저장
for _ in range(L):
    sec, direction = map(str, input().split())
    snake_info.append([int(sec), direction])

# 오른쪽 회전
right_dict = {
    '[0, 1]': [1, 0],
    '[1, 0]': [0, -1],
    '[0, -1]': [-1, 0],
    '[-1, 0]': [0, 1],
}

# 왼쪽 회전
left_dict = {
    '[0, 1]': [-1, 0],
    '[1, 0]': [0, 1],
    '[0, -1]': [1, 0],
    '[-1, 0]': [0, -1],
}

def no_apple(cx, cy): # 사과가 없으면 몸 길이 변화 없음 (머리와 꼬리 이동)
    stack.append([cx, cy])
    stack.pop(0)

def yes_apple(cx, cy): # 사과가 있으면 사과를 없애고 몸 길이 길어짐 (머리만 이동)
    arr[cx][cy] = 0
    stack.append([cx,cy])

start = [0, 0] # 출발 시점

stack = [] # 뱀이 있는 위치들
stack.append(start)

d = [0, 1] # 처음에 움직이는 방향 (오른쪽 이동)

cnt = 0 # 초 계산

flag = True # while 문 종료 조건 생성
while flag:
    if len(snake_info) > 0: # snake_info 가져오기
        sec, direction = snake_info.pop(0)
    else: # 없으면 최대 길이로 sec 받기 (벽에 부딪힐 때까지 진행해야 하기 때문)
        sec = N + cnt
    
    dx, dy = d # 뱀이 움직이는 진행 방향
    for _ in range(sec-cnt): # 같은 방향으로 움직이는 시간
        nx, ny = stack[-1][0] + dx, stack[-1][1] + dy # 다음으로 움직였을 때 뱀의 위치

        if not (0 <= nx < N and 0 <= ny < N) \
            or ([nx, ny] in stack): # 벽에 부딪히거나 자기자신의 몸과 부딪히면 게임 중지
            flag = False
            cnt += 1 # 벽에 부딪히려면 이동해야하기 때문에 +1 해줘야 함
            break
        
        if arr[nx][ny] == 0: # 사과가 없을 때
            no_apple(nx, ny)
        else: # 사과가 있을 때
            yes_apple(nx, ny)

        cnt += 1 # 이동 시간 업데이트

    # 이동 시간이 끝났으면 방향 전환
    if direction == 'L': # 왼쪽으로 전환
        d = left_dict[str(d)]
    else: # 오른쪽으로 전환
        d = right_dict[str(d)]

print(cnt)
