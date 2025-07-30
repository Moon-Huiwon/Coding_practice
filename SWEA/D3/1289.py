#%%
T = int(input())
for t in range(T):
    data = list(int(char) for char in input())
    init = [0] * len(data)

    cnt = 0
    while data != init:
        for i in range(len(data)):
            if data[i] == init[i]:
                continue
            else:
                if init[i] == 0:
                    init[i:] = [1] * len(init[i:])
                else:
                    init[i:] = [0] * len(init[i:])
                cnt += 1
    print(f'#{t+1} {cnt}')
# %%