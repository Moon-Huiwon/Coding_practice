# 정답 코드
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

n = int(input())

# input 수열 받기
input_sequence = [int(input()) for _ in range(n)]

# stack 리스트 생성 (push하는 애들 넣는 부분)
stack = []
# 결과 값 저장하는 리스트 생성 (+/- 저장)
result = []
# current 1~n까지 값을 갖는다. (초기값은 1로 설정)
current = 1
# 주어진 수열을 만들 수 있는지 확인하는 변수
possible = True
# 주어진 input 수열의 값을 하나씩 받아온다.
for num in input_sequence:
    # current 값이 num보다 작거나 같으면 전부 push (push하는 코드)
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    
    # stack의 마지막 값과 num이 같으면 pop (pop하는 코드)
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    
    # 그렇지 않으면 주어진 수열을 만들 수 없음
    else:
        possible = False

if possible == True:
    for s in result:
        print(s)
else:
    print('NO')


#%%
# 틀린 코드
import copy

n = int(input())

input_sequence = [int(input()) for _ in range(n)]

check_list = copy.deepcopy(input_sequence)
num_list = [i for i in range(1, n+1)]

stack = []
answer = []
print_answer = []
while num_list:
    num = num_list.pop(0)

    # 순차적으로 push와 pop을 하는 방법이 필요함
    # 현재 코드는 push와 pop이 여기저기에 사용되면서 스택이 뒤섞이는 오류 발생
    if input_sequence[0] == num:
        answer.append(num)
        print_answer.append('+')
        print_answer.append('-')
        input_sequence.pop(0) # 여기서도 pop

    
    elif len(stack) > 0 and input_sequence[0] == stack[-1]:
        answer.append(stack.pop())
        print_answer.append('-')
        input_sequence.pop(0) # 여기서도 pop 하면서 문제 발생
        print_answer.append('+')
        stack.append(num)

    else:
        stack.append(num)
        print_answer.append('+')

while stack:
    answer.append(stack.pop())
    print_answer.append('-')

if answer == check_list:
    for i in range(len(print_answer)):
        print(print_answer[i])
else:
    print('NO')