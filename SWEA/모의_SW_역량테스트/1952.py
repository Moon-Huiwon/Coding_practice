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
    

