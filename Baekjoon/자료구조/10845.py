import sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    cmd = list(input().rstrip().split())
    if len(q) == 0:
        if cmd[0] in ['pop', 'front', 'back']:
            print(-1)
        elif cmd[0] == 'empty':
            print(1)
    else:
        if cmd[0] == 'pop':
            print(q.pop(0))
        elif cmd[0] == 'empty':
            print(0)
        elif cmd[0] == 'front':
            print(q[0])
        elif cmd[0] == 'back':
            print(q[-1])
    
    if cmd[0] == 'push':
            q.append(int(cmd[1]))
    elif cmd[0] == 'size':
            print(len(q))