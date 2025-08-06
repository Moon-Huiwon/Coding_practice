for _ in range(10):
    # 테스트 케이스 번호
    T = int(input())

    # 2차원 배열 생성
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 행의 합의 최대값 찾기
    row_max = 0
    for i in range(100):
        if sum(arr[i]) > row_max:
            row_max = sum(arr[i])

    # 열의 합의 최대값 찾기
    col_max = 0
    for j in range(100):
        # 각 열의 합을 구하기 위해 initialize
        tmp = 0
        for i in range(100):
            tmp += arr[i][j]
        # 최대값 업데이트
        if tmp > col_max:
            col_max = tmp

    # 오른쪽 아래로 향하는 대각선의 합
    ## 초기값 설정
    right_x = 0
    for i in range(100):
        right_x += arr[i][i]

    # 왼쪽 아래로 향하는 대각선의 합
    ## 초기값 설정
    left_x = 0
    ## 왼쪽 아래로 향하기 때문에 delta 값 (1, -1)로 설정
    dx, dy = (1, -1)
    x, y = (0, 99)
    for _ in range(100):
        left_x += arr[x][y]

        # x, y값 이동되게 없데이트
        x, y = x + dx, y + dy

    print(f'#{T} {max(row_max, col_max, right_x, left_x)}')