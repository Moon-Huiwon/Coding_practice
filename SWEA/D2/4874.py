T = int(input())
for t in range(T):
    stack = []
    input_value = list(map(str, input().split()))
    possible = True
    for s in input_value:
        # '.'일때 종료
        if s == '.':
            break
        
        # stack에 숫자 쌓기
        elif s not in '+-*/':
            stack.append(int(s))
        else:
            # 숫자가 2개 이상 쌓여있으면, (연산자 사용하려면 숫자 2개 필요)
            # pop을 통해 숫자 가져오기
            # 각 연산자 기호에 맞게 계산하기
            if len(stack) > 1:
                second_value = stack.pop()
                first_value = stack.pop()
                if s == '+':
                    stack.append(first_value + second_value)
                elif s == '-':
                    stack.append(first_value - second_value)
                elif s == '*':
                    stack.append(first_value * second_value)
                else:
                    # '/' 사용시 float 형식으로 나타남
                    # 따라서 '//' 사용할 것 (int로 표현하기 위해)
                    stack.append(first_value // second_value) 
            
            # 숫자가 1개 이하이면 가능한 계산식이 아님
            else:
                possible = False
    # 계산이 가능하고 len(stack)이 1이면 정답이 도출가능
    if possible and len(stack) == 1:
        print(f'#{t+1} {stack[-1]}')
    # 아니면 에러
    else:
        print(f'#{t+1} error')
                