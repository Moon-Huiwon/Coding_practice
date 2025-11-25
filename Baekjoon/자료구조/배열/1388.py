import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

ans = 0

A = 0
B = [0] * M
for i in range(N):
    if A > 0:
        ans += 1
        A = 0
    for j in range(M):
        if arr[i][j] == '-':
            A = 1
            
            ans += B[j]
            B[j] = 0
                
        else:
            # '|'일 경우
            B[j] = 1
            
            # '-'일 경우
            ans += A
            A = 0
 
ans += A
ans += sum(B)
print(ans)
