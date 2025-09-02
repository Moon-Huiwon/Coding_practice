T = int(input())

for t in range(T):
    N = float(input()) # 실수값 받기

    tmp = []
    while len(tmp) < 13: # 12자리 이내일 때까지 돌리기
        N *= 2 # 2배로 계산
        if N > 1.0: # 정수 자리가 1이면 이진수 1 입력
            tmp.append('1')
            N -= 1.0
        elif 0.0 < N < 1.0:# 정수 자리가 0이면 이진수 0 입력
            tmp.append('0')
        
        else: # N이 1.0이거나 0.0이면 이진수 입력 마무리
            tmp.append(str(int(N))) # 정수 자리 입력
            print(f'#{t+1} {"".join(tmp)}') # 결과 도출
            break
        
    if len(tmp) >= 13: # 13자리 이상인 경우 overflow 출력
        print(f'#{t+1} overflow')