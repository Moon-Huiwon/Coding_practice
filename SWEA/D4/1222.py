for t in range(10):
    length = int(input())
    cal_str = input().rstrip()

    # 후위 표기식으로 바꾸기
    change_cal = ''
    
    # 연산자 저장하는 stack
    stack = []
    for c in cal_str:
        # stack이 비어있고 연산자이면 stack에 넣기
        if len(stack) == 0 and c == '+':
            stack.append(c)
        # stack에 연산자가 있고, 현재 연산자이면
        # pop을 활용하여 후위 표기식에 넣고
        # 현재 c(+)를 stack에 다시 넣기
        elif len(stack) > 0 and c == '+':
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
        if c != '+':
            stack.append(int(c))
        # stack에 숫자가 2개 이상 쌓여있으면 두 값을 끌고 와서
        # 연산자 적용하기 (덧셈)
        else:
            if len(stack) > 1:
                second_value = stack.pop()
                first_value = stack.pop()
                stack.append(first_value + second_value)
    
    # 테스트 케이스가 전부 옳은 계산식이므로
    # stack[0]으로 답 출력
    print(f'#{t+1} {stack[0]}')