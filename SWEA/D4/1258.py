T = int(input())
for t in range(T):
    n = int(input())
    ans = [] # 행X열 오름차순, 같을 경우 행 기준으로 오름차순 정리
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]

    ans = []
    delta = [(1, 0), (0, 1)]
    for i in range(n):
        for j in range(n):
            
            if visited[i][j] == 0:

                if arr[i][j] == 0:
                    visited[i][j] = 1
                
                else:
                    row = 1
                    col = 1
                    for dx, dy in delta:
                        nx, ny = i+dx, j+dy
                        while 1:
                            if 0 <= nx < n and 0 <= ny < n and \
                                arr[nx][ny] > 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                nx += dx
                                ny += dy

                                if dx == 1:
                                    row += 1
                                else:
                                    col += 1

                            else:
                                break

                    for p in range(i, i+row):
                        visited[p][j:j+col] = [1]*(col)
                
                    ans.append([row*col, row, col])      

    ans.sort()
    print(f'#{t+1} {len(ans)}', end=" ")
    for i in range(len(ans)):
        print(ans[i][1], end=" ")
        print(ans[i][2], end=" ")
    print()

#%%
# 강사님 코드
tests = int(input())

for test_case in range(1, tests + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answers = []
    for i in range(n):
        for j in range(n):
            # 현재 칸이 0이라면 다음 칸으로
            if arr[i][j] == 0:
                continue
            
            # 현재 지점에서 0이 나올때까지 오른쪽으로
            col = j
            while col < n and arr[i][col] != 0:
                col += 1

            # 현재 지점에서 0이 나올때까지 아래로
            row = i
            while row < n and arr[row][j] != 0:
                row += 1

            # 현재 지점과 오른쪽 끝, 아래 끝 사이의 거리가 answers에 들어간다.
            answers.append([row-i, col-j])

            # 해당 공간을 0으로 갱신한다.
            for x in range(i, row):
                for y in range(j, col):
                    arr[x][y] = 0
    
    # 두개의 아이템을 비교하는 함수
    # a와 b를 비교했을 때,
    # a가 b보다 작으면 음수
    # a가 b보다 크면 양수
    # 같으면 0
    def cmp_func(a, b):
        # a와 b를 비교하는 첫 기준은 넓이
        a_area = a[0] * a[1]
        b_area = b[0] * b[1]
        # 근데 둘이 같으면 [0]을 기준으로 정렬
        if a_area == b_area:
            return a[0] - b[0]
        else:
            return a_area - b_area
    
    # cmp_to_key 함수 import
    from functools import cmp_to_key
    answers.sort(key=cmp_to_key(cmp_func))
    print(f'#{test_case} {len(answers)} {answers}')