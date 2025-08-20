T = int(input())
for t in range(T):
    # N: 화덕에 구울 수 있는 피자 개수
    # M: 총 피자 개수 
    N, M = map(int, input().split())
    # 각 피자의 치즈 양
    cheese = list(map(int, input().split()))
    # 각 피자의 번호와 치즈 양 리스트로 만들어서 저장
    idx_cheese = []
    for i in range(M):
        idx_cheese.append([i+1, cheese[i]])
    
    # 화덕에 넣어서 구울 피자
    bake_pizza = []
    for i in range(N):
        pizza = idx_cheese.pop(0)
        bake_pizza.append(pizza)
    
    # 화덕에 넣어서 구울 피자가 1개 일 때까지 반복문
    i = 0
    while bake_pizza.count(0) < N - 1:
        # 원형으로 동작하기 위해
        i %= N
        # 피자가 비어있는 공간이 아니면
        if bake_pizza[i] != 0:
            # 피자 치즈 양을 절반으로 줄이기
            bake_pizza[i][1] //= 2

            # 치즈 양이 0이고, 대기 중인 피자가 있다면
            # 해당 위치에 대기 중인 피자 넣기
            if bake_pizza[i][1] == 0 and len(idx_cheese) > 0:
                bake_pizza[i] = idx_cheese.pop(0)
            # 대기 중인 피자가 없다면
            # 빈공간으로 설정 (0)
            elif bake_pizza[i][1] == 0:
                bake_pizza[i] = 0
        
        # 다음 순서로 이동    
        i += 1
    
    # 마지막에 남은 피자 확인
    ans = 0
    for i in range(len(bake_pizza)):
        if bake_pizza[i] != 0:
            ans = bake_pizza[i][0]
            break
        
    print(f'#{t+1} {ans}')