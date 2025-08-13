import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

while True:
    # 개행문자 제거할 것
    sentence = input().rstrip()
    
    if sentence == '.':
        break
    
    stack = []
    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                # 아니면 stack에 쌓기
                stack.append(')')
                break
        elif s == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                # 아니면 stack에 쌓기
                stack.append(']')
                break
        
    if len(stack) == 0:
        print('yes')
    else:
        print('no')