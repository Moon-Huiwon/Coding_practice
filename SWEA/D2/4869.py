# 재귀함수 활용
def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n-1) + 2*fibo(n-2)

T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t+1} {fibo(N // 10)}')

# DP 활용
def fibo(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n +1):
        dp[i] = dp[i-1] + 2*dp[i-2]
    
    return dp[n]

T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t+1} {fibo(N // 10)}')
