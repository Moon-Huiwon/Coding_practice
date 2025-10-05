import sys
sys.setrecursionlimit(10**7)

def dfs(x, y):
    global cnt
    if (x, y) in visited or arr[x][y]==0:
        return
    
    visited.add((x, y))
    cnt += 1
    
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < h and 0 <= ny < w):
            continue
        
        if (nx, ny) in visited:
            continue
        
        if arr[x][y] == 0:
            continue
        
        dfs(nx, ny)
        

while 1:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    arr = [list(map(int ,input().split())) for _ in range(h)]
    visited = set()
    ans = 0
    for i in range(h):
        for j in range(w):
            cnt = 0
            dfs(i, j)
            if cnt > 0:
                ans += 1
    
    print(ans)