# 시간초과 확인해야함

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
