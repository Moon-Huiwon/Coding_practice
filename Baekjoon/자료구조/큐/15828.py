from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
packet = deque()
while 1:
    info = int(input())

    if info == -1:
        break

    if info > 0 and len(packet) < N:
        packet.append(info)
    elif info == 0:
        packet.popleft()

if len(packet) == 0:
    print('empty')
else:
    print(*packet)


