#%%
# 시간 초과 발생
# list방식으로 시간복잡도 느림
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
x = int(input())

cnt = 0

while num_list:
    # O(n)
    a_i = num_list.pop(0)
    a_j = x - a_i
    
    if a_j in num_list: # O(n): 존재 여부 확인
        num_list.remove(a_j) # O(n): 리스트에서 값 제거
        cnt += 1

print(cnt)

#%%
import sys
input = sys.stdin.readline
n = int(input())
num_set = set((map(int, input().split()))) # 중복 제거

x = int(input())

remain_num = set() # 쌍이 되지 못한 값 저장

cnt = 0
for a_i in num_set:
    a_j = x - a_i
    
    if a_j in remain_num: # O(1): 쌍이 되지 못한 값 중에 있는 지 확인
        remain_num.remove(a_j) # O(1): set에서 제거
        cnt += 1  
    else:
        remain_num.add(a_i)  # O(1): set에 저장

print(cnt)

# %%
# 투포인터 방식
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

# 양 끝에 포인터 두기
i = 0
j = n-1
count = 0

# 두 포인터가 교차할 때 종료
# 그 이후의 (j, i) 쌍은 이미 (i, j) 쌍에서
# 처리된 경우들임
while i < j:
    sum_tmp = arr[i] + arr[j]
    if sum_tmp == x:
        count += 1
        i += 1
        j -= 1
    elif sum_tmp > x:
        j -= 1
    else:
        i += 1

print(count)
# 출처: https://velog.io/@ledcost/백준-3273-파이썬-두-수의-합-실버-3-투-포인터