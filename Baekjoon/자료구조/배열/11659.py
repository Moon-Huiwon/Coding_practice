#%%
# sys.stdin.readline으로 받아야 시간초과 안남**
# input은 내부적으로 sys.stdin.readline()을 호출하면서도 추가로 많은 부가 처리를 함
# input은 입력값을 확인하고 처리하는 인터프리터 수준의 기능이 포함되어 있어서 오버헤드가 큼

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
cumulative_num = [0] * (N+1) # 누적합을 저장하기 위한 리스트

for i in range(1, N+1):
    cumulative_num[i] = cumulative_num[i-1] + num_list[i-1] # 숫자의 누적합 계산


for _ in range(M):
    i, j = map(int, input().split())
    print(cumulative_num[j] - cumulative_num[i-1]) # 누적합을 가지고 정답 도출

#%%
# 기존 내 코드: 시간초과 발생
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
for _ in range(M):
    i, j = map(int, input().split())
    print(sum(num_list[i-1:j])) # 리스트 슬라이싱 후 합계를 계산할 때 시간 초과 발생 