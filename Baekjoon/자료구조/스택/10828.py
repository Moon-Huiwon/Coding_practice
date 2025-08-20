import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
