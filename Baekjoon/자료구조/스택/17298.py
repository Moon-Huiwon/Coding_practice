# 시간 초과
N = int(input())
A = list(map(int, input().split()))

while A:
    a_value = A.pop(0)
    neg_value = 0
    for num in A:
        if num > a_value:
            neg_value = num
            break
    
    if neg_value > 0:
        print(neg_value, end=" ")
    else:
        print(-1, end=" ")

#%%
# stack으로 시간 복잡도 낮춤 (stack으로 내가 푼 방식)
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []
answer = []
# 시간복잡도를 낮추기 위해 거꾸로 확인하기
for i in range(N-1,-1,-1):

    # stack에 쌓인게 없다면 오른쪽에 조건에 맞는 값이 없다는 것
    # 따라서 -1을 answer에 넣고 stack에 해당 값 넣기
    if len(stack) == 0:
        stack.append(A[i])
        answer.append(-1)
    else:
        # stack[-1] <= A[i] 이면 조건이 만족할 때까지 pop()으로 값 제거
        while stack and stack[-1] <= A[i]: # 등호 작성***
            stack.pop()
        
        # stack에 값이 존재하고 stack[-1] > A[i]이면 조건에 맞는 값 찾음
        # 해당 값을 answer에 넣고, stack에 현재 값 넣기
        if stack and stack[-1] > A[i]:
            answer.append(stack[-1])
            stack.append(A[i])
        
        # while 구문을 돌렸을 때 조건에 맞는 값이 안나오면
        # -1을 answer에 넣고, 해당 값 stack에 넣어주기
        else:
            answer.append(-1)
            stack.append(A[i]) # stack에 넣어주기***

# 거꾸로 되어있으므로 reverse 진행하고 출력
print(*answer[::-1])      
        