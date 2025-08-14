import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    
    # 흑과 백의 차이를 abs()를 활용하기 위해서 100으로 초기값 설정
    arr = [[100]*N for _ in range(N)]
    
    # 가운데 row와 col
    c = N // 2
    
    # 정가운데 배치 (초기값)
    # 흑돌 배치
    arr[c-1][c] = 1
    arr[c][c-1] = 1
    # 백돌 배치
    arr[c-1][c-1] = 2
    arr[c][c] = 2

    for _ in range(M):
        # 돌을 놓는 행과 열 값 받기
        row, col, color = map(int, input().split())
        
        # python은 0~3이고, 입력값은 1~4이므로 1씩 줄여주기
        row -= 1
        col -= 1
        
        # 해당 위치의 (흑/백) 돌 놓기
        arr[row][col] = color

        # 방향: 위,아래,왼쪽,오른쪽, 대각선(총4개)
        # 총 방향은 8개 확인
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dx, dy in delta:
            # ex) '흑백백흑'인 경우 백을 흑으로 바꿔주어야하기 때문에
            # 바꿔야하는 돌들을 stack에 넣기
            stack = []
            nx , ny = row + dx, col + dy
            # 돌은 범위를 넘어가선 안된다.
            while 0 <= nx < N and 0 <= ny < N:
                # 지금 놓은 돌과 다른 색상이면 stack에 저장 (둘의 차이를 가지고 확인)
                # 그리고 같은 방향으로 더 이동 (dx, dy 그대로 더 해주기)
                if abs(arr[nx][ny] - color) == 1:
                    stack.append((nx, ny))
                    nx += dx
                    ny += dy
                
                # 만약 같은 색상이 나오면 
                # stack에 쌓인 돌들을 같은 색상으로 변경
                elif arr[nx][ny] == color:
                    while stack:
                        ch_row, ch_col = stack.pop()
                        arr[ch_row][ch_col] = color
                    break
                
                # 초기값인 100이 나오면 멈추고 다른 방향 탐색
                else:
                    break
    
    # 최종적으로 나온 arr에서 흑돌, 백돌 개수 세기
    black = 0
    white = 0
    for i in range(N):
        black += arr[i].count(1)
        white += arr[i].count(2)

    print(f'#{t+1} {black} {white}')