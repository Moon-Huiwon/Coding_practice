T = int(input())
for t in range(T):
    N, nums = map(str, input().rstrip().split())

    tmp = []
    for num in nums:
        ans = bin(int(num, 16))[2:] # 10 진수 -> 16진수 -> 2진수
        tmp.append('0'*(4-len(ans)) + ans) # 앞자리 0 입력
    
    print(f'#{t+1} {"".join(tmp)}') # 결과 도출