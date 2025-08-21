from collections import deque
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
weight = deque(map(int, input().split()))

stack = deque([0] * w)
cnt = 0
while weight:
    if len(stack) == w:
        stack.popleft()
    
    if sum(stack) + weight[0] <= L:
            stack.append(weight[0])
            weight.popleft()
    else:
        stack.append(0)
    
    cnt += 1
    
print(cnt+len(stack))