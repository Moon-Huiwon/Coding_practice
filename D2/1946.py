#%%
T = int(input())

for t in range(T):
    N = int(input())
    arr = []
    print(f'#{t+1}')
    for i in range(N):
        string, cnt = map(str, input().split())
        cnt = int(cnt)

        for _ in range(cnt):
            if len(arr) < 10:
                arr.append(string)
            else:
                print(''.join(map(str, arr)))
                arr = []
                arr.append(string)
        if i == N-1:
            print(''.join(map(str, arr)))

# %%
