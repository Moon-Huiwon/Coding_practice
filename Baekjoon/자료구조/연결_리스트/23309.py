# 시간초과 (풀이 중,,,,,)
import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
station = list(map(int, input().split()))

# 여기서 시간초과 발생 / 전체를 쓰려고 했는데,, 불필요한 리스트 개수라 시간초과,,,
max_num = 1000001
pre_num = deque([[] for _ in range(max_num)])
post_num = deque([[] for _ in range(max_num)])

for i in range(N):
    pre_num[station[i]].append(station[i-1])
    
    if i == N-1:
        post_num[station[i]].append(station[0])    
    else:
        post_num[station[i]].append(station[i+1])

for _ in range(M):
    cmd_list = list(map(str, input().split()))
    cmd = cmd_list[0]
    i = int(cmd_list[1])

    if len(cmd_list) > 2:
        j = int(cmd_list[2])
    
    if cmd == 'BN':
        num = post_num[i].pop()
        print(num)
        if len(post_num[j]) == 0:

            post_num[i].append(j)
            post_num[j].append(num)

            pre_num[num].pop()
            pre_num[num].append(j)
            pre_num[j].append(i)
        
    elif cmd == 'BP':
        num = pre_num[i].pop()
        print(num)
        if len(pre_num[j]) == 0:
            pre_num[i].append(j)
            pre_num[j].append(num)

            post_num[num].pop()
            post_num[num].append(j)
            post_num[j].append(i)
    
    elif cmd == 'CN':
        print(post_num[i].pop())
    
    else:
        print(pre_num[i].pop())

