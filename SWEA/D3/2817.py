def backtracking(start, value):
    global ans
    if value > K:
        return
    
    if value == K:
        ans += 1
        return

    for i in range(start, N):
        backtracking(i+1, value+A[i])

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    backtracking(0,0)
    print(f'#{t+1} {ans}')