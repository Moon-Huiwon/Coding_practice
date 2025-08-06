T = int(input())
for t in range(T):
    # 칠할 영역의 개수
    N = int(input())

    # 10x10 행렬 생성
    matrix = [[0]*10 for _ in range(10)]

    # 칠할 영역의 개수만큼 돌리기
    for _ in range(N):
        # [r1, c1] 부터 [r2, c2]까지 color 색칠 (1이면 빨강 2이면 파랑)
        r1, c1, r2, c2, color = map(int, input().split())

        # 해당하는 칸에 색깔 색칠
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                matrix[i][j] += color

    answer = 0
    # 같은 색인 영역은 겹치지 않으며 빨강과 파랑이 겹쳐지면 해당 칸의 숫자는 3으로 나타난다.
    # 따라서 3를 count 하여 정답 도출
    for i in range(10):
        answer += matrix[i].count(3)

    print(f'#{t+1} {answer}')
