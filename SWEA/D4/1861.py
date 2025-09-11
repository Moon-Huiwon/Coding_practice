import sys
sys.stdin = open('input.txt')

def move_room(x, y): # 이동할 수 있을 만큼 이동
    global cnt_room
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # 4방향 이동
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N \
            and A[nx][ny] == A[x][y] + 1:
            cnt_room += 1 # 방 이동 개수 업데이트
            move_room(nx, ny) # 다음 방으로 이동
        
T = int(input())
for t in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans_cnt = 0
    ans_start = N**2
    for i in range(N):
        for j in range(N):
            cnt_room = 1 # 출발해야하는 방부터 카운트 시작
            move_room(i, j) # 방 이동

            if cnt_room > ans_cnt: 
                ans_cnt = cnt_room # 최대 방 개수 업데이트
                ans_start = A[i][j] # 시작 지점 업데이트
            elif cnt_room == ans_cnt: # 최대 방 개수가 동일한 경우
                ans_start = min(ans_start, A[i][j]) # 시작 지점의 수가 가장 작은 값으로 변경

    print(f'#{t+1} {ans_start} {ans_cnt}')