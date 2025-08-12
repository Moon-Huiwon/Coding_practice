T = int(input())
for t in range(T):
    # 문자열 받기
    string = list(input())
    # 스택 생성
    stack = []
    # stack에 문자가 쌓여있고, 마지막에 넣은 문자가 s와 같으면 pop (반복되는 문자 제거)
    # 다르면 stack에 쌓기
    for s in string:
        if len(stack) > 0 and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    
    print(f'#{t+1} {len(stack)}')