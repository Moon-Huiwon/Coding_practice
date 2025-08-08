T = int(input())
for t in range(T):
    # 첫번째 문자 받기
    str1 = list(input())
    # 두번째 문자 받기
    str2 = list(input())
    # count 값이 max인 값 초기 설정
    max_cnt = 0
    for s in str1:
        # 각 문자의 cnt 계산
        cnt = 0
        cnt += str2.count(s)
        # max_cnt 업데이트
        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{t+1} {max_cnt}')