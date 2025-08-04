#%%
T = int(input())

for t in range(T):
    N = int(input())
    a = list(map(int, input().split()))

    min_value = min(a)
    max_value = max(a)
    print(f'#{t+1} {max_value - min_value}')