T = int(input())
for t in range(T):
    # input 값 받기
    input_str = list(input())
    # stack 생성
    stack = []
    for s in input_str:
        # open_string은 stack에 쌓기
        if s == '(' or s == '{':
            stack.append(s)
        # close_string은 open_string이 바로 앞에 있으면 제거
        # 아니면 stack에 쌓기
        elif s == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
        elif s == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s)
    
    # 제대로 구성되어 있다면 stack에 비어있어야 한다.
    if len(stack) == 0:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')