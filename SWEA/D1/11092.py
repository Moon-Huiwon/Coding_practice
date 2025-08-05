#%%
T = int(input())
for t in range(T):
    N = int(input())
    a = list(map(int, input().split()))

    min_value = min(a)
    max_value = max(a)

    min_idx = a.index(min_value)
    max_idx = max([idx for idx in range(N) if a[idx] == max_value])

    print(f'#{t+1} {abs(min_idx - max_idx)}')