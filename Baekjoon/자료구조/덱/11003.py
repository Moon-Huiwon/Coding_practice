# 시간초과
import sys
input = sys.stdin.readline

from collections import deque

N, L = map(int, input().split())
nums = list(map(int, input().split()))
tmp = deque()
for num in nums:
    if len(tmp) < L:
        tmp.append(num)
        print(min(tmp)) # 시간초과 발생
    else:
        tmp.popleft()
        tmp.append(num)
        print(min(tmp)) # 시간초과 발생

#%%
# 정답 코드
import sys
input = sys.stdin.readline

from collections import deque

N, L = map(int, input().split())
nums = list(map(int, input().split()))
tmp = deque()

for i in range(N):

    while tmp and tmp[0][0] <= i - L: # 범위 외의 숫자를 제거
        tmp.popleft()
    
    while tmp and tmp[-1][1] >= nums[i]: # 큰 수 제거 (큰 수는 필요없음)
        tmp.pop()
    
    # tmp에 숫자 넣기
    tmp.append((i, nums[i])) # 튜플이 리스트보다 메모리를 덜 차지함***
    # tmp.append([i, nums[i]]) # 리스트로 저장할 시 시간초과 및 메모리 초과 발생***

    print(tmp[0][1], end=" ")
    