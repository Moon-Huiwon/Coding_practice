#%%
money_list = [500, 100, 50, 10, 5, 1]
pay_price = int(input())

remain_price = 1000 - pay_price

cnt = 0

while money_list:
    money = money_list.pop(0)
    cnt += remain_price // money
    remain_price %= money

print(cnt)