T = int(input())
for t in range(T):
    # 문자 받기
    str = list(input())
    reversed_str = []
    
    for i in range(len(str)-1, -1, -1):
        reversed_str.append(str[i])
    
    # 거꾸로 읽어도 같으면 1 출력 / 아니면 0 출력
    if str == reversed_str:
        print(f'#{t + 1} 1')
    else:
        print(f'#{t + 1} 0')