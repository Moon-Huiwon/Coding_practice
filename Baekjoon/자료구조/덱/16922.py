# 정답코드
# 원래 코드 -> 시간초과 발생 (범위 설정이 너무 컸다...)
from collections import deque
N = int(input())

values = [1, 5, 10,50] # 주어진 로마 숫자의 값
stack = deque() # 숫자 저장
sum_set = set() # 숫자 합 저장 # 중복은 제거하므로 set으로 설정

def dfs(depth, start):
    
    if depth == N: # N만큼 돌았다면 stack에 4개 쌓여있으므로 sum_set에 합계 저장
        sum_set.add(sum(stack))
        return
    
    for i in range(start, 4): # 범위 설정 유의 
        stack.append(values[i]) # stack에 값 저장
        dfs(depth+1, i) # 다음 단계로 넘어가고 start는 i로 설정*** # 전체 다 돌면 시간초과***
        stack.pop() # 백트래킹
        
dfs(0, 0)
print(len(sum_set))