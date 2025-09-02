# pypy로 진행할 때 돌아감
# python으로 진행하면 시간초과,,,
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
station = list(map(int, input().split()))

max_num = 1000001
pre_num = [0] * max_num
post_num = [0] * max_num

for i in range(N):
    pre_num[station[i]] = station[i-1]
    post_num[station[i]] = station[i+1] if i < N-1 else station[0]

result = []

for _ in range(M):
    cmd_list = list(map(str, input().split()))
    cmd = cmd_list[0]
    i = int(cmd_list[1])

    if len(cmd_list) > 2:
        j = int(cmd_list[2])
    
    if cmd == 'BN':
        station_num = post_num[i]

        post_num[i] = j
        post_num[j] = station_num

        pre_num[station_num] = j
        pre_num[j] = i
    
    elif cmd == 'BP':
        station_num = pre_num[i]

        pre_num[i] = j
        pre_num[j] = station_num

        post_num[station_num] = j
        post_num[j] = i

    elif cmd == 'CN':
        station_num = post_num[i] # 폐쇄할 station
        post_num[i] = post_num[station_num] # 폐쇄한 station의 다음 역
        pre_num[post_num[station_num]] = i
    
    else:
        station_num = pre_num[i]
        pre_num[i] = pre_num[station_num]
        post_num[pre_num[station_num]] = i

    result.append(str(station_num))

print('\n'.join(result))

#%%
# 시간초과
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
station = list(map(int, input().split()))

pre_num = {} # 이전 역 저장
post_num = {} # 다음 역 저장

for i in range(N):
    pre_num[station[i]] = station[i-1]
    post_num[station[i]] = station[i+1] if i < N-1 else station[0]

result = []

for _ in range(M):
    cmd_list = list(map(str, input().split()))
    cmd = cmd_list[0]
    i = int(cmd_list[1])
    if len(cmd_list) > 2:
        j = int(cmd_list[2])
    
    if cmd == 'BN':
        station_num = post_num[i]

        post_num[i] = j
        post_num[j] = station_num

        pre_num[station_num] = j
        pre_num[j] = i
    
    elif cmd == 'BP':
        station_num = pre_num[i]

        pre_num[i] = j
        pre_num[j] = station_num

        post_num[station_num] = j
        post_num[j] = i
    
    elif cmd == 'CN':
        station_num = post_num[i] # 폐쇄할 station
        post_num[i] = post_num[station_num] # 폐쇄한 station의 다음 역
        pre_num[post_num[station_num]] = i

        del post_num[station_num], pre_num[station_num] # 시간초과 발생
    
    else:
        station_num = pre_num[i]
        pre_num[i] = pre_num[station_num]
        post_num[pre_num[station_num]] = i

        del post_num[station_num], pre_num[station_num] # 시간초과 발생
    
    result.append(str(station_num))

print('\n'.join(result))