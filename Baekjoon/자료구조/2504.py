string = input().rstrip()
stack = []
for s in string:
    # 열린 괄호면 stack에 저장
    if s == '(' or s == '[':
        stack.append(s)
    
    # 닫힌 작은 괄호일때
    elif s == ')':
        # stack[-1]이랑 짝이 맞으면 pop 진행
        if len(stack) > 0 and stack[-1] == '(':
            stack.pop()
            # stack[-1]의 값이 정수이면 해당 값에 더해주고
            if len(stack) > 0 and type(stack[-1]) == int:
                stack[-1] += 2
            # 정수 값이 아니면 stack에 2 넣기
            else:
                stack.append(2)

        # stack[-1]이 정수이고, stack[-2]가 열린 괄호일 때
        elif len(stack) > 1 and stack[-2] == '(' and type(stack[-1]) == int:
            # 정수 값에 곱하기 2
            num = stack.pop() * 2
            # 열린 괄호 없애기 위한 pop
            stack.pop()
            # stack[-1]이 숫자면 더해주고
            if len(stack) > 0 and type(stack[-1]) == int:
                stack[-1] += num
            # 아니면 stack에 값 넣어주기
            else:
                stack.append(num)
        
        # 아무것도 아니면 stack에 쌓기
        else:
            stack.append(s)
    
    elif s == ']':
        if len(stack) > 0 and stack[-1] == '[':
            stack.pop()
            if len(stack) > 0 and type(stack[-1]) == int:
                stack[-1] += 3
            else:
                stack.append(3)
        
        elif len(stack) > 1 and stack[-2] == '[' and type(stack[-1]) == int:
            num = stack.pop() * 3
            stack.pop()
            if len(stack) > 0 and type(stack[-1]) == int:
                stack[-1] += num
            else:
                stack.append(num)
        else:
            stack.append(s)

# stack의 길이가 1이고 그게 정수이면 올바른 괄호
if len(stack) == 1 and type(stack[0]) == int:
    print(stack[0])
else:
    print(0)

#%%
bracket = input()
length = len(bracket)
stack = []
tmp = 1
res = 0
i = 3
for i in range(length):
    b = bracket[i]   
    if b == '(':
        tmp *= 2
        stack.append(b)
    elif b == '[':
        tmp *= 3
        stack.append(b)

    elif b == ')':
        if not stack or stack[-1] == '[':
            res = 0
            # break
        if bracket[i-1] == '(':
            res += tmp
        tmp //= 2
        stack.pop()  
    else:
        if not stack or stack[-1] == '(':
            res = 0
            # break
    # [()]의 경우 ] 직전 문자가 )이므로 더하지 않고 넘어감
    # 단, 이 경우는 오류는 아님 >> 지금까지 계산한거 한번만 해주면 되기 때문에...
        if bracket[i-1] == '[':
            res += tmp
        tmp //= 3
        stack.pop() 