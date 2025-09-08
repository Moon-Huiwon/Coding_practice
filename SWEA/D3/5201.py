T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    w_i = list(map(int, input().split())) # 화물 무게
    t_i = list(map(int, input().split())) # 트럭 적재용량

    w_i.sort(reverse=True) # 내림차순으로 설정
    t_i.sort(reverse=True) # 내림차순으로 설정

    ans = 0
    for i in range(M): # 트럭 개수 만큼 반복문 설정
        
        # 현재 가장 무거운 화물 무게 가져오기
        if len(w_i) > 0:
            weight = w_i.pop(0)
        else:
            weight = 0
            break
        
        # 트럭에 넣을 수 있는 최대 화물 무게 찾기
        while t_i[i] < weight:
            if len(w_i) > 0:
                weight = w_i.pop(0)
            else:
                weight = 0
                break
        
        # 전체 무게를 구하기 위해서 ans에 화물 무게 더해주기
        ans += weight
    
    print(f'#{t+1} {ans}')