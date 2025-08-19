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