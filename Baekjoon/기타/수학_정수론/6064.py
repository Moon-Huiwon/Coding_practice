# 시간 초과
def find_kying(init_x, init_y):
    global cnt
    while 1:
        if init_x == x and init_y == y:
            return cnt
        
        if init_x == M and init_y == N:
            return -1
        
        # if M > N and init_y == y and init_x > x:
        #     return -1
        # if N > M and init_x == x and init_y > y:
        #     return -1
        
        else:
            init_x += 1
            init_y += 1
            cnt += 1
            
            if init_x > M:
                init_x = 1
            
            if init_y > N:
                init_y = 1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    cnt = 1
    ans = find_kying(1, 1)
    print(ans)
    
#%%

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    ans = -1
    
    k = x
    while k <= M * N:
        if (k - y) % N == 0:  # y와 같은 해인지 확인
            ans = k
            break
        k += M
    print(ans)
