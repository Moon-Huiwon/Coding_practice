# import sys
# sys.stdin = open("input.txt")

# 암호 비율 (앞에 0은 체크 안함)
# 조건: 암호코드들이 붙어있는 경우는 존재하지 않는다 (최소 1칸 이상의 빈 공간이 존재)
# 따라서 0의 암호 비율 계산에 넣지 않는다.
decode = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9,
}

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(set([input().strip() for _ in range(N)])) # 배열 받기(중복 제거)
    
    tmp = [] # 암호코드로 보이는 것 저장하는 리스트
    for code in arr:
        result = bin(int(code, 16))[2:].lstrip('0') # 이진수로 바꾸고 왼쪽 0은 제거 (왼쪽 0의 비율은 확인하지 않기 때문에)
        n1 = n2 = n3 = 0 # 비율을 확인하기 위한 세팅
        code_number = ''
        for c in result:
            if c == '1' and n2 == 0: # 연속적인 1의 개수 찾기
                n1 += 1
            elif c =='0' and n1 != 0 and n3 == 0: # 다음으로 연속적인 0의 개수 찾기
                n2 += 1
            elif c == '1' and n2 != 0: # 다음으로 연속적인 1의 개수 찾기
                n3 += 1
            elif c == '0' and n3 != 0: # 숫자 0이 다시 나오면 암호 코드 숫자 확인 끝
                r = min(n1, n2, n3) # 비율 찾기 위한 최소값 찾기
                ratio = f'{n1//r}{n2//r}{n3//r}' # 최소값을 나눠서 비율 구하기
                num = decode[ratio] # 비율에 해당하는 숫자 받기
                code_number += str(num) # code_number에 저장하기
                
                if len(code_number) == 8:
                    if code_number not in tmp: # tmp에 없으면 저장하기
                        tmp.append(code_number)
    
                    code_number = '' # 암호코드 다시 찾기 위해 리셋
                
                n1 = n2 = n3 = 0 # 암호코드에 들어갈 숫자 찾기 위해 리셋
    
    answer = 0
    for check in tmp: # 암호코드 후보 전부 확인하기
        odd = 0 # 홀수
        even = 0 # 짝수
        for k in range(8):
            if (k+1) % 2 == 1:
                odd += int(check[k])
            else:
                even += int(check[k])
        
        if (odd * 3 + even) % 10 == 0: # 정상적인 암호코드
            answer += odd + even
    
    print(f'#{t+1} {answer}')