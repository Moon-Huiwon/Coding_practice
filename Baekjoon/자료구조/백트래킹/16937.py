import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())

stickers = []
for _ in range(N):
    Ri, Ci = map(int, input().split())
    if Ri <= max(H, W) and Ci <= max(H, W):    
        stickers.append([Ri, Ci])

ans = 0
def backtracking(idx):
    global ans
    if idx >= len(stickers):
        return
    
    for i in range(idx+1, len(stickers)):
        tmp1 = [stickers[idx][0] + stickers[i][0], max(stickers[idx][1], stickers[i][1])]
        tmp2 = [stickers[idx][0] + stickers[i][1], max(stickers[idx][1], stickers[i][0])]
        
        tmp3 = [max(stickers[idx][0], stickers[i][0]), stickers[idx][1] + stickers[i][1]]
        tmp4 = [max(stickers[idx][0], stickers[i][1]), stickers[idx][1] + stickers[i][0]]
        
        if (min(tmp1) <= min(H, W) and max(tmp1) <= max(H, W)) \
            or (min(tmp2) <= min(H, W) and max(tmp2) <= max(H, W)) \
                or (min(tmp3) <= min(H, W) and max(tmp3) <= max(H, W)) \
                    or (min(tmp4) <= min(H, W) and max(tmp4) <= max(H, W)):
                ans = max(ans, stickers[idx][0]*stickers[idx][1] + stickers[i][0]*stickers[i][1])
    
    backtracking(idx+1)
            
backtracking(0)
print(ans)