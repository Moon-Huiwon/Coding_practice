T = int(input())
for t in range(T):

    # 문자열 받기
    str1 = input()
    str2 = input()

    # str1이 str2에 들어있는지 확인하는 코드
    if str1 in str2:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')
