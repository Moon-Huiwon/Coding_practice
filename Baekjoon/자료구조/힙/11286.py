import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")

import heapq

tmp = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x < 0:
        heapq.heappush(tmp, [-x, x])
    elif x > 0:
        heapq.heappush(tmp, [x, x])
    else:
        if len(tmp) == 0:
            print(0)
        else:
            ans = heapq.heappop(tmp)    
            print(ans[1])
        