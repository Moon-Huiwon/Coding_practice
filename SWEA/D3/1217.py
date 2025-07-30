#%%
for _ in range(10):
    test_case_num = int(input())

    N, M = map(int, input().split())

    cnt = 0
    def power(num, N=N, M=M):
        global cnt
        if cnt < M-1:
            num *= N
            cnt += 1
            return power(num)
        else:
            return num
        
    answer = power(N)
    print(f'#{test_case_num} {answer}')
