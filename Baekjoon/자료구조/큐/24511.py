# 시간초과
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queuestack = list(map(int, input().split()))
nums = deque(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

# 중첩 for문 -> 시간초과
for num in C:    
    input_num = num
    for i in queuestack:
        # queue 선입선출
        if i == 0:
            nums.append(input_num)
            input_num = nums.popleft()
        # stack 후입선출
        # input_num 그대로
        else:
            nums.append(nums.popleft())
    print(input_num, end=" ")

#%%
# 시간초과
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queuestack = list(map(int, input().split()))
nums = deque(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

# 중첩 for문 -> 시간초과
for num in C:
    input_num = num
    for i in range(N):
        if queuestack[i] == 0:
            input_num, nums[i] = nums[i], input_num
    
    print(input_num, end=" ")

#%%
# 정답코드
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queuestack = list(map(int, input().split()))
nums = deque(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

# stack은 input_num이 바뀌지 않으므로 의미 없음
# 따라서 queue 작업을 진행하는 값만 가져온다
# 단, queue는 선입선출이므로 마지막 값이 선입이 되어야한다.
# 따라서 range를 거꾸로 진행한다. ***
# ex) input(2) -> queue(1) -> stack(1) -> stack(1) -> queue(4) -> 정답:4
queue_value = deque()
for i in range(N-1, -1, -1):
    if queuestack[i] == 0:
        queue_value.append(nums[i])

# queue는 선입선출이므로 C의 값들은 마지막에 더해준다.
for num in C:
    queue_value.append(num)
    print(queue_value.popleft(), end=" ")
    