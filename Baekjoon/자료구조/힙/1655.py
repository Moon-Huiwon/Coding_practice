import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")

import heapq
N = int(input())

left_heap = []
right_heap = []

for _ in range(N):
    num = int(input())

    if len(left_heap) == 0 or num < -left_heap[0]:
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
    
    # 왼쪽과 오른쪽 차이가 1로 유지해야 함
    if len(left_heap) < len(right_heap): # 왼쪽이 더 많이 push 되어야 함
        heapq.heappush(left_heap, -heapq.heappop(right_heap))
    elif len(left_heap) > len(right_heap) + 1:
        heapq.heappush(right_heap, -heapq.heappop(left_heap))

    
    print(-left_heap[0])



