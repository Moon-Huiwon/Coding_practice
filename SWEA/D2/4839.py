
T = int(input())
for t in range(T):
		# P: 총 페이지 수
    P, A, B = map(int, input().split())
		
		# A와 B가 탐색하는 횟수 각각 설정
    A_explore = 0
    B_explore = 0
		
		# 1쪽으로 설정 (초기값)
    A_l = 1
    # 맨마지막 페이지 설정 (초기값)
    A_r = P
    
    while True:
		    # 탐색을 시작했으므로 +1
        A_explore += 1
        # 중간 페이지 확인
        c = int((A_l+A_r)/2)
        # 찾았으면 멈춤
        if A == c:
            break
        # 찾는 페이지가 중간 페이지보다 크면 l(찾아볼 첫 페이지)를 c로 설정
        elif A > c:
            A_l = c
        # 찾는 페이지가 중간 페이지보다 작으면 r(찾아볼 마지막 페이지)를 c로 설정
        else:
            A_r = c
        
        # l >= r인 경우 찾을 수 없는 경우 이므로 break
        if A_l >= A_r:
            break
		
		# A와 동일하게 코드 구성
    B_l = 1
    B_r = P
    while True:
        B_explore += 1
        c = int((B_l+B_r)/2)
        if B == c:
            break
        elif B > c:
            B_l = c
        else:
            B_r = c
        
        if B_l >= B_r:
            break

    if A_explore == B_explore:
        print(f'#{t+1} {0}')
    elif A_explore < B_explore:
        print(f'#{t+1} A')
    else:
        print(f'#{t+1} B')

