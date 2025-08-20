# 시간초과
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip()))
remove_cnt = 0

stack = []
while remove_cnt < K:
    num = numbers.pop(0)
    
    while stack and stack[-1] < num:
        stack.pop()
        remove_cnt += 1
        
        if remove_cnt == K:
            break
    
    stack.append(num)

ans = stack + numbers
print(''.join(map(str, ans)))

#%%
# 정답 코드
## pop()을 두번 사용하는 부분에서 시간 초과가 발생한 것으로 생각
## 따라서 for문을 활용하는 방식으로 바꿨다.
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip()))
remove_cnt = 0
remain_idx = len(numbers)

stack = []
for i in range(N):
    if remove_cnt < K:
        # stack[-1] < numbers[i]이면 계속 pop() 하도록 진랭
        while stack and stack[-1] < numbers[i]:
            stack.pop()
            remove_cnt += 1
            
            # remove_cnt == K이면 더 이상 작동하면 안되므로 break
            if remove_cnt == K:
                break
        # 현재 선택된 숫자는 stack에 저장한다
        # 다음 숫자와 비교할 수 있게 
        stack.append(numbers[i])
    else:
        # remove_cnt == K 이면 작동을 멈추고
        # stack에 넣지 못한 숫자들을 확인하기 위해
        # for문이 돌아가지 않은 첫번째 index 추출
        remain_idx = i
        break

# 실수 했던 부분
# remove_cnt < K 인 채로 for문이 끝날 경우를 생각 안함(ex. 7755)
# 이 경우 K-remove_cnt 만큼 뒤에 있는 숫자 제거가 필요
if remove_cnt < K:
    ans = stack + numbers[remain_idx:] # stack과 numbers[remain_idx:] 합치기
    ans = ans[:-(K-remove_cnt)] # K-remove_cnt 만큼 더 제거 (제거가 덜 된 횟수만큼 뒤에 숫자 제거)
else:
    ans = stack + numbers[remain_idx:]

print(''.join(map(str, ans)))

