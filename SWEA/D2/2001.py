T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    # 파리 숫자로 구성된 matrix
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # max 값 initialize
    max_value = 0
    # i: 행의 시작점 위치
    for i in range(N-M+1):
        # j: 열의 시작점 위치
        for j in range(N-M+1):

            # M*M 영역의 파리 갯수 initialize
            value = 0
            # p: 행을 M개 만큼 이동
            for p in range(M):
                # q: 열을 M개 만큼 이동
                for q in range(M):
                    value += matrix[i+p][j+q]

            # value가 max_value보다 크면 max값 재설정
            if value > max_value:
                max_value = value

    print(f'#{t+1} {max_value}')
