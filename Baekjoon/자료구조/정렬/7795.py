# 시간초과
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    if max(A) < min(B):
        print(cnt)
        continue
    else:
        for a in A:
            for b in B:
                if a > b:
                    cnt += 1
        
        print(cnt)
#%%
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort()
    cnt = 0
    
    j = 0
    for i in range(N):
        while j < M and A[i] > B[j]:
            j += 1
        cnt += j
    
    print(cnt)