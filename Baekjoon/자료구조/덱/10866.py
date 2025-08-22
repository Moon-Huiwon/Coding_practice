from collections import deque
import sys
input = sys.stdin.readline

stack = deque()
N = int(input())
for _ in range(N):
    cmd = list(input().split())
    str_cmd = cmd[0]
    
    if str_cmd == 'push_front':
        num = cmd[1]
        stack = deque([num]) + stack
    elif str_cmd == 'push_back':
        num = cmd[1]
        stack.append(num)
    
    if len(stack) > 0:
        if str_cmd == 'pop_front':
            print(stack.popleft())
        elif str_cmd == 'pop_back':
            print(stack.pop())
        elif str_cmd == 'size':
            print(len(stack))
        elif str_cmd == 'empty':
            print(0)
        elif str_cmd == 'front':
            print(stack[0])
        elif str_cmd == 'back':
            print(stack[-1])
    else:
        if str_cmd == 'pop_front':
            print(-1)
        elif str_cmd == 'pop_back':
            print(-1)
        elif str_cmd == 'size':
            print(len(stack))
        elif str_cmd == 'empty':
            print(1)
        elif str_cmd == 'front':
            print(-1)
        elif str_cmd == 'back':
            print(-1)