import sys
sys.stdin = open('input.txt')

import copy

def greedy(month, total_price, plan):
    global min_price
    
    if month == 12: # 중단
        min_price = min(min_price, total_price)
        return

    if plan[month] == 0:
        greedy(month+1, total_price, plan) # month만 증가시켜서 재귀호출
    else:
        for i in range(3):
            new_plan = copy.deepcopy(plan) # plan 다시 사용하기 위해 deepcopy
            if i == 0:
                new_plan[month] = new_plan[month]*prices[i] # 1일 이용권
                greedy(month+1, total_price+new_plan[month], new_plan)
            elif i == 1: # 1달 이용권
                new_plan[month] = prices[i]
                greedy(month+1, total_price+prices[i], new_plan)
            else: # 3달 이용권
                new_plan[month:month+3] = [prices[i],0,0]
                greedy(month+1, total_price+prices[i], new_plan)
            
T = int(input())
for t in range(T):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_price = prices[-1]
    greedy(0,0, plan)
    print(f'#{t+1} {min_price}')

#%%
# 강사님 코드 (DP)

T = int(input())
for tc in range(1, T + 1):
    # 이용권 가격들 (1일, 1달, 3달, 1년)
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # 12개월 이용 계획 (0은 버린다)
    days = [0] + list(map(int, input().split()))

    dp = [0] * 13  # 누적해서 저장해 나아갈 dp 리스트 (그림과 동일)
    # 시작점 초기화 (1월, 2월)
    # 1월의 가격 (1일권 구매 vs 1달권 구매)
    dp[1] = min(days[1] * cost_day, cost_month)
    # 2월의 가격 = 1월의 최소 가격 + 2월의 최소 가격 (1일권 구매 vs 1달권 구매)
    dp[2] = dp[1] + min(days[2] * cost_day, cost_month)

    # 3월~12월은 반복하면서 계산
    for month in range(3, 13):
        # N월의 최소 비용 후보
        # 1. (N-3)월에 3개월 이용권을 구입한 경우
        # 2. (N-1)월의 최소 비용 + 1일권 구매
        # 3. (N-1)월의 최소 비용 + 1달권 구매
        dp[month] = min(dp[month-3] + cost_month3
                        , dp[month-1] + (days[month] * cost_day)
                        , dp[month-1] + cost_month)

    # 12월의 누적 최소 금액 vs 1년권
    answer = min(dp[12], cost_year)
    print(f'#{tc} {answer}')

