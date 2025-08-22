for t in range(10):
    length = int(input())
    cal_str = input().rstrip()

    # 후위 표기식으로 바꾸기
    change_cal = ''
    
    # 연산자 저장하는 stack
    stack = []
    cal_dict = {'+' : 1, 
               '*' : 2}
    
    for c in cal_str:
        # stack이 비어있고 연산자이면 stack에 넣기
        if len(stack) == 0 and c in cal_dict:
            stack.append(c)

        # stack에 연산자가 있고, 현재 값이 연산자이면서
        # stack[-1]보다 우선순위가 높다면 stack에 쌓는다.
        elif len(stack) > 0 and c in cal_dict \
            and cal_dict[c] > cal_dict[stack[-1]]:
            stack.append(c)
        # stack[-1]과 같거나 우선순위가 낮다면
        # stack.pop()하여 후위 표기식에 저장한다
        # 그 다음 현재 연산자를 stack에 넣어준다.
        elif len(stack) > 0 and c in cal_dict \
            and cal_dict[c] <= cal_dict[stack[-1]]:
            change_cal += stack.pop()
            stack.append(c)
        # 피연산자이면 후위 표기식에 넣기
        else:
            change_cal += c
    
    # 마지막에 stack에 있는 연산자 후위 표기식에 넣기
    while stack:
        change_cal += stack.pop()

    # 후위 표기식을 가지고 계산하기
    # 숫자들 쌓아놓는 stack
    stack = []
    for c in change_cal:
        # 피연산자이면 stack에 쌓기
        if c not in cal_dict:
            stack.append(int(c))
        # stack에 숫자가 2개 이상 쌓여있으면 두 값을 끌고 와서
        # 연산자 적용하기 (덧셈/곱셈)
        else:
            if len(stack) > 1:
                if c == '+':
                    second_value = stack.pop()
                    first_value = stack.pop()
                    stack.append(first_value + second_value)
                else:
                    second_value = stack.pop()
                    first_value = stack.pop()
                    stack.append(first_value * second_value)
    
    # 테스트 케이스가 전부 옳은 계산식이므로
    # stack[0]으로 답 출력
    print(f'#{t+1} {stack[0]}')


#%%
# 강사님 코드
expression = input()
# 후위표기법 변환을 위해 stack을 만들자
stack = []
# 변환된 후위표기법을 표기하기 위한 변수
result_expr = ''

# 각 토큰(숫자와 연산자)를 하나씩 확인한다.
for token in expression:
    # 숫자는 그대로 출력
    if token not in '*+':
        result_expr += token
        # 다음 토큰으로
        continue
    # 여기부터는 연산잔 판단
    # 1. stack이 비어있을 경우 그냥 푸시
    if not stack:
        stack.append(token)
    # 2. 아닌데 지금 토큰이 *인 경우
    elif token =='*':
        # 나보다 우선순위가 높거나 같은애가 제일 위에 있을 동안에
        # *가 나왔으므로 +가 나오거나 스택이 빌때까지 반복한다.
        while stack and stack[-1] == '*':
            # 출력한다.
            result_expr += stack.pop()
        #  그 후 내가 들어간다.
        stack.append(token)
    # 아니면 +다
    else:
        # 나보다 우선순위 낮은애는 없으니 다 뺀다
        while stack:
            result_expr += stack.pop()
        # 그 후 내가 들어간다.
        stack.append(token)

# stack을 마저 비운다
while stack:
    result_expr += stack.pop()

# 변환 결과 확인
# print(result_expr)

# 후위표기 계산
# 숫자는 스택에 넣고
# 연산자가 나오면 스택에서 숫자 두개 빼고 계산
for token in result_expr:
    # 만약 숫자라면
    if token not in '*+':
        stack.append(int(token))
        continue
    
    # 스택에서 숫자를 두개를 빼온다.
    right = stack.pop()
    left = stack.pop()

    # 연산자에 맞춰서 연산한다.
    if token == '+':
        stack.append(left + right)
    else:
        stack.append(left*right)

print(stack.pop())