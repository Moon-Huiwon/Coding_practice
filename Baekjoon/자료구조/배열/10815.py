#%%
import sys
input = sys.stdin.readline

N = int(input())
sanguen = set(map(int, input().split())) # 시간초과 문제로 인해 set으로 설정
M = int(input())
check_list = list(map(int, input().split()))



answer = []
for num in check_list:
    if num in sanguen: # 여기서 시간단축 (set은 탐색 속도가 O(1) )
        answer.append(1)
    else:
        answer.append(0)

print(*answer)

#%%
import sys
input = sys.stdin.readline

N = int(input())
sanguen = list(map(int, input().split())) # 시간 초과 발생
M = int(input())
check_list = list(map(int, input().split()))



answer = []
for num in check_list:
    if num in sanguen: # 여기서 시간 초과 발생 (리스트는 선형 탐색: O(N) )
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
