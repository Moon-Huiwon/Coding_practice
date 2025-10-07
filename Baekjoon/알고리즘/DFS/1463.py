def dfs(num, cnt):
    global min_cnt
    
    if min_cnt <= cnt:
        return
    
    if num == 1:
        min_cnt = min(min_cnt, cnt)
        return
    
    if num % 6 == 0:
        for next_num in [num//3, num//2, num-1]:
            dfs(next_num, cnt+1)
            
    elif num % 3 == 0:
        for next_num in [num//3, num-1]:
            dfs(next_num, cnt+1)
    
    elif num % 2 == 0:
        for next_num in [num//2, num-1]:
            dfs(next_num, cnt+1)
    else:
        dfs(num-1, cnt+1)
    
N = int(input())
min_cnt = 10**6
dfs(N, 0)
print(min_cnt)