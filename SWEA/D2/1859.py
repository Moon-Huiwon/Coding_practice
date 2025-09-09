T = int(input())
for t in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    # 최대 매매가 넣을 리스트
    stack = []
    # 최대 이익 초기값
    profit = 0
    
    # 거꾸로 진행해야 이익 계산 가능
    # ex) 11312 일 경우 [1,1,3] [1,2] 이렇게 따로 이익을 내야함
    # 따라서 최대 이익을 stack에 저장하고 
    # stack에 넣은 값보다 작은 값은 전부 이때 파는 걸로 하여 이익 창출
    # stack에 넣은 값보다 큰 값이 주어지면 stack.pop을 통해 없애고
    # stack에 더 큰 값 저장하여 이때 판매하도록 설정
    for p in range(N-1, -1, -1):
        # 이익 창출
        if len(stack) > 0 :
            if stack[-1] > prices[p]:
                profit += stack[-1] - prices[p]
            # 최고 매매가 다시 설정
            else:
                stack.pop()
                stack.append(prices[p])
        # 최고 매매가 설정
        else:
            stack.append(prices[p])
    
    print(f'#{t+1} {profit}')

#%%
T = int(input())
for t in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    ans = 0
    max_value = 0
    for i in range(N-1, -1, -1):
        if max_value < prices[i]:
            max_value = prices[i]
        else:
            ans += max_value - prices[i]
    
    print(f'#{t+1} {ans}')