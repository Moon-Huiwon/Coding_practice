# 7개 비트의 암호화된 숫자들
code_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())
for t in range(T):
    N, M = map(int, input().split()) # 세로 크기 / 가로 크기

    arr = [input() for _ in range(N)] # 암호 코드 입력받기

    def start_row(): # 암호가 시작되는 행 찾기
        for i in range(N):
            if arr[i] == '0'*M: # 전부 0으로 구성되어있으면 암호 없음
                continue
            else: # 그렇지 않으면 암호 코드 존재
                break
        return i # 암호 코드 존재하는 행 값 추출

    i = start_row()

    tmp = arr[i][::-1] # 암호는 0으로 시작하고 1로 끝나기 때문에 뒤집어서 암호를 찾아야 함
    
    j = tmp.index('1') # 1이 시작되는 index 찾기

    value_list = []
    while j + 7 < M:
        code_segment = tmp[j:j+7][::-1] # 7개씩 코드 분활하기
        if code_segment == '0'*7: # 암호 X
            break
        if code_segment in code_dict: # 암호 O
            value_list.append(code_dict[code_segment]) # 암호코드 숫자 입력
            j += 7 # 다음 암호 탐색하기 위해
    
    value_list = value_list[::-1] # 거꾸로 저장되어있기 때문에 원래 방향으로

    odd = 0 # 홀수
    even  = 0 # 짝수
    for k in range(len(value_list)):
        if (k + 1) % 2 == 1: 
            odd += value_list[k]
        else:
            even += value_list[k]

    if (odd * 3 + even) % 10 == 0: # 올바른 암호코드
        print(f'#{t+1} {odd + even}')
    else: # 잘못된 암호코드
        print(f'#{t+1} {0}')