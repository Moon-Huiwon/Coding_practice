import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(10**5)

def dfs(y, x):
    global cnt
    
    if (y, x) in check_idx:
        return
    
    check_idx.append((y, x))
    cnt += 1

    for dy, dx in [(0,1),(1,0),(-1,0),(0,-1)]:
        ny, nx = y+dy, x+dx
        if 0 <= ny < M and 0 <= nx < N \
            and (ny, nx) not in check_idx \
                and (ny, nx) in exist_idx:
                    dfs(ny, nx)
        
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    exist_idx = []
    for _ in range(K):
        Y, X = map(int, input().split())
        exist_idx.append((Y, X))
    check_idx = []
    ans = 0
    for cy, cx in exist_idx:
        cnt = 0
        dfs(cy, cx)
        if cnt > 0:
            ans += 1
    
    print(ans)
        