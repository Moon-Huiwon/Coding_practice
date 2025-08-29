T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    cnt = 0 # 스위치 조작 횟수
    for i in range(N):
        if cnt % 2 == 0 and A[i] != B[i]: # 짝수번(원래랑 동일한 전등상태) 조작 했는데 다르면 스위치 조작
            cnt += 1        
        elif cnt % 2 == 1 and A[i] == B[i]: # 홀수번(원래랑 반대인 전등상태) 조작 했는데 같으면 스위치 조작
            cnt += 1
    
    print(f'#{t+1} {cnt}')