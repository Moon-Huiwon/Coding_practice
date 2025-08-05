#%%
T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    M = list(map(int, input().split()))

    # 정류장을 idx로 사용하고, 충전기 여부를 0과 1를 사용해서 표시
    charge_list = [0] * (N+1)
    for charge_num in M:
        charge_list[charge_num] = 1

    # 출발지 (and 충전한 정류장)
    start_num = 0

    # 충전 횟수
    charge_cnt = 0

    # 충전한 정류장에서 K 만큼 이동한게 마지막 정류장이거나 그 이상이면 끝 (충전 필요 X)
    # 그렇지 않으면 충전이 필요하므로 코드 작동
    while start_num + K < N:

        # 충전기가 K 범위 안에 있는지 확인
        if 1 in charge_list[start_num+1:start_num+1+K]:
            
            # 충전 횟수 업데이트
            charge_cnt += 1
            
            # 충전한 정류장 세팅
            for num in range(start_num+K, start_num, -1):
                if charge_list[num] == 1:
                    start_num = num
                    break
        # 없으면 종점에 도착할 수 없으므로 0 출력
        else:
            charge_cnt = 0
            break
    print((f'#{t+1} {charge_cnt}'))
# %%
