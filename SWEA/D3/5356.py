T = int(input())
for t in range(T):
    # arr 입력 받기 (총 다섯 줄로 이루어져 있다고 되어있음)
    arr = [list(input()) for _ in range(5)]

    # 최대 길이 확인
    max_col_cnt = 0
    for i in range(5):
        if len(arr[i]) > max_col_cnt:
            max_col_cnt = len(arr[i])

    # 문자열 넣을 리스트 생성
    answer = []
    # 최대 길이까지 loop 돌리기
    for j in range(max_col_cnt):
        # 단, arr[i]의 길이가 j보다 커야 입력값이 존재
        # arr[i]의 길이가 j와 같거나 작으면 입력값이 존재 X
        # ex) arr[i] = [1, 2, 3] / max_col_cnt = 5이면 j = [0, 1, 2, 3, 4]
        # len(arr[i]) == 3 이고, arr[i][2]까지 출력 가능 따라서 j보다 커야 입력값이 존재 (등호가 들어가면 out of index)
        for i in range(5):
            if len(arr[i]) > j:
                answer.append(arr[i][j])
            else:
                continue

    print(f'#{t+1} {"".join(answer)}')