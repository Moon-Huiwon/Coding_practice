T = int(input())
for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]

    answer = 1

    flag = True

    while flag:
        # 각 행의 숫자가 중복이 있는지 확인
        for i in range(9):
            arr_cnt = [0] * 10
            for j in range(9):
                num = arr[i][j]
                arr_cnt[num] += 1

            # 중복이 있으면 중지
            if max(arr_cnt) > 1:
                flag = False
                answer = 0
                break

        while flag:
            # 각 열의 숫자가 중복이 있는지 확인
            for j in range(9):
                arr_cnt = [0] * 10
                for i in range(9):
                    num = arr[i][j]
                    arr_cnt[num] += 1

                # 중복이 있으면 중지
                if max(arr_cnt) > 1:
                    flag = False
                    answer = 0
                    break

            while flag:
                # 3x3 격자 크기에 중복이 있는지 확인
                ## i: 행의 시작점을 3간격으로 조정
                ## j: 열의 시작점을 3간격으로 조정
                for i in range(0, 9, 3):
                    for j in range(0, 9, 3):
                        arr_cnt = [0] * 10

                        ## p: 행의 시작점부터 3개의 행 사용
                        ## q: 열의 시작점부터 3개의 열 사용
                        for p in range(i, i+3):
                            for q in range(j, j+3):
                                num = arr[p][q]
                                arr_cnt[num] += 1

                        # 중복이 있으면 중지
                        if max(arr_cnt) > 1:
                            flag = False
                            answer = 0
                            break

                flag = False

    print(f'#{t+1} {answer}')
