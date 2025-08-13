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

#%%
# 강사님 코드
n = int(input())

# 첫줄은 무조건 1 하나
pascal = [
    [1],
]

# 두번째 (1번째) 부터 n번째까지 반복해서 채워넣을 것이다.
for i in range(1, n):
    # i번째 줄의 첫번째 숫자는 1이다.
    row = [1]
    
    # i번째 줄의 '1 ~ i-1' 칸 까지는
    for j in range(1, i):
        # 이전줄(i-1)의 이전칸(j-1) + 이전줄(i-1)의 현재칸(j)를 합한 값이다.
        row.append(pascal[i-1][j-1] + pascal[i-1][j])

    # i번째 줄의 마지막 숫자는 1이다.
    row.append(1)
    # 줄이 완성되었으며 pascal에 넣기
    pascal.append(row)
    
for row in pascal:
    print(row)
