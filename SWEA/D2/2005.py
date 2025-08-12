T = int(input())
for t in range(T):
    # 삼각형 크기 받기
    N = int(input())
    # 테스트 케이스 프린트 하기
    print(f'#{t+1}')
    # 숫자를 넣어둘 스택 생성
    stack = []
    for _ in range(N):
        
        # 스택이 비어있으면 1을 집어넣기 (첫 번째 줄은 항상 숫자 1이다.)
        if len(stack) == 0:
            stack.append(1)
        
        # 스택에 값이 있다면 스택에 맨 앞에 있는 1을 빼고 전부 없앨 수 있도록 pop을 활용
        # 따라서 len(stack) - 1 만큼 for문 작동
        # 마지막 stack 값을 pop으로 뽑고, 저장된 stack의 마지막 값과 더한 값을 더해주는 방식 사용
        # stack에 바로 저장할 시 문제가 생김
        # stack에 1만 남길 때 까지 append 하지 않고 add_values에 값을 저장
        # for문이 끝난 후 저장된 add_values 값을 stack에 저장
        else:
            add_values = []
            for _ in range(len(stack)-1):
                last_value = stack.pop()
                value = last_value + stack[-1]
                add_values.append(value)

            stack.extend(add_values)
            # 마지막에 1을 추가로 넣어줘야 함.
            stack.append(1)
    
        print(*stack)
