T = int(input())
for t in range(T):
    # 문자 받기
    str = list(input())
    
    # 거꾸로 읽어도 같으면 1 출력 / 아니면 0 출력
    if str == str[::-1]:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')