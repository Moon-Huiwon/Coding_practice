# open 괄호 리스트 생성
open_string = ['(', '[', '{', '<']
# close 괄호 리스트 생성
close_string = [')', ']', '}', '>']
for t in range(10):
    # 길이 받기
    length = int(input())
    # 문자열 받기 (괄호로 구성)
    string = list(input())
    # 스택 생성
    stack = []
    for s in string:
        # open_string에 있으면 push
        if s in open_string:
            stack.append(s)
        # close_string에 있으면 pop 할 수 있음
        else:
            # close_string의 open_string 짝을 찾기 위해 index 확인
            index = close_string.index(s)
            # stack에 문자가 쌓여있고,
            # 마지막에 쌓인 괄호가 close_string의 짝(open_string)이라면 pop
            if len(stack) > 0 and stack[-1] == open_string[index]:
                stack.pop()
            # 그렇지 않다면 stack에 쌓기
            else:
                stack.append(s)
    
    if len(stack) == 0:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')
