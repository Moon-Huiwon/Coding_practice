T = int(input())
for t in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    ans = 0
    tmp = 1
    for i in range(N-1):
        if C[i]+1 <= C[i+1]: # 연속으로 커지면 tmp + 1
            tmp += 1
        else:
            ans = max(ans, tmp) # 커지지 않았으면 ans 업데이트
            tmp = 1 # 초기화
    
    ans = max(ans, tmp) # 최대값 찾기

    print(f'#{t+1} {ans}')