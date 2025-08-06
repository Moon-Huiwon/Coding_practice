T = int(input())
for t in range(T):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    # 단어가 들어갈 자리의 수 초기 설정
    answer = 0

    # 행 자리 확인 (가로에 자리 있는지 확인)
    for i in range(N):
        # K개수 만큼 자리가 있는지 확인하는 값
        check = 0
        for j in range(N):
            # 자리가 비어있으면(1) check + 1
            if puzzle[i][j] == 1:
                check += 1

            # 자리가 막혀있으면(0) check가 K만큼인지 확인 (11110 불가능 1110 가능)
            # 그렇다면 answer + 1
            # check를 다시 초기화
            else:
                if check == K:
                    answer += 1

                check = 0
        # 끝까지 갔을 때 check가 K만큼인지 확인
        # 그렇다면 answer + 1
        if check == K:
            answer += 1

    # 열 자리 확인 (세로에 자리 있는지 확인)
    for j in range(N):
        # K개수 만큼 자리가 있는지 확인하는 값
        check = 0
        for i in range(N):
            # 자리가 비어있으면(1) check + 1
            if puzzle[i][j] == 1:
                check += 1

            # 자리가 막혀있으면(0) check가 K만큼인지 확인 (11110 불가능 1110 가능)
            # 그렇다면 answer + 1
            # check를 다시 초기화
            else:
                if check == K:
                    answer += 1

                check = 0
        # 끝까지 갔을 때 check가 K만큼인지 확인
        # 그렇다면 answer + 1
        if check == K:
            answer += 1

    print(f'#{t+1} {answer}')