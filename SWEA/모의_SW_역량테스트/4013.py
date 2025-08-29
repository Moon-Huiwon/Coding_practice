import sys
sys.stdin = open("input.txt")

from collections import deque

T = int(input())
for t in range(T):
    K = int(input())
    magnet = [deque(map(int, input().split())) for _ in range(4)]
    cmd = []
    for _ in range(K):
        cmd.append(list(map(int, input().split())))
    
    for c in cmd:
        num = c[0] - 1
        direction = c[1]

        move_magnet = [num]
        
        # 오른쪽
        right = num
        while right + 1 < 4:
            if magnet[right][2] != magnet[right+1][-2]:
                move_magnet.append(right+1)
                right += 1
            else:
                break
        
        # 왼쪽
        left = num
        while left - 1 >= 0:
            if magnet[left][-2] != magnet[left-1][2]:
                move_magnet.append(left-1)
                left -= 1
            else:
                break

        for m in move_magnet:
            if (num + m) % 2 == 0:
                magnet[m].rotate(direction)
            else:
                magnet[m].rotate(direction*(-1))
                
    ans = 0
    for i in range(4):
        if i == 0:
            if magnet[i][0] == 1:
                ans += 1
        elif i == 1:
            if magnet[i][0] == 1:
                ans += 2
        elif i == 2:
            if magnet[i][0] == 1:
                ans += 4
        elif i == 3:
            if magnet[i][0] == 1:
                ans += 8
    
    print(f'#{t+1} {ans}')