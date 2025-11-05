# 시간초과
N = int(input())

cards = []
for _ in range(N):
    card = int(input())
    cards.append(card)

cnt = 0
ans = float('inf')
for num in set(cards):
    if cards.count(num) > cnt:
        cnt = cards.count(num)
        ans = num
    elif cards.count(num) == cnt:
        if num < ans:
            ans = num

print(ans)

#%%
# 해결코드
N = int(input())

card_dict = {}

for _ in range(N):
    card = int(input())
    if str(card) not in card_dict.keys():
        card_dict[str(card)] = 1
    else:
        card_dict[str(card)] += 1

max_cnt = max(card_dict.values())

ans = float('inf')
for key, value in card_dict.items():
    if value == max_cnt and int(key) < ans:
        ans = int(key)

print(ans)

#%%