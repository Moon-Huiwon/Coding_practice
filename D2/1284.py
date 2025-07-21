#%%
T = int(input())
for t in range(T):
    P, Q, R, S, W = map(int, input().split())

    price_list = []
    price_list.append(W * P)

    if W <= R :
        price_list.append(Q)
    else:
        price_list.append(Q + (W - R) * S)

    print(f'#{t+1} {min(price_list)}')
# %%
