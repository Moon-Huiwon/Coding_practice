import heapq
import sys
input = sys.stdin.readline

tmp = []

N = int(input())
for _ in range(N):
    num = int(input())
    if num > 0:
        heapq.heappush(tmp, num)
    else:
        if len(tmp) == 0:
            print(0)
        else:
            print(heapq.heappop(tmp))
