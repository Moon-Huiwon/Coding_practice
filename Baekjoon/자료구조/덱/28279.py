# deque의 appendleft 기능***
from collections import deque
import sys
input = sys.stdin.readline

stack = deque()
N = int(input())
for _ in range(N):
    cmd_list = list(map(int, input().split()))
    cmd = cmd_list[0]

    if cmd == 1:
        num = cmd_list[1]
        stack.appendleft(num) # stack = deque([num]) + stack 이용시 시간초과 발생
        continue
    elif cmd == 2:
        num = cmd_list[1]
        stack.append(num)
        continue
    
    if len(stack) > 0:
        if cmd == 3:
            print(stack.popleft())
        elif cmd == 4:
            print(stack.pop())
        elif cmd == 5:
            print(len(stack))
        elif cmd == 6:
            print(0)
        elif cmd == 7:
            print(stack[0])
        elif cmd == 8:
            print(stack[-1])
    else:
        if cmd in [3, 4, 7, 8]:
            print(-1)
        elif cmd == 5:
            print(0)
        elif cmd == 6:
            print(1)
        