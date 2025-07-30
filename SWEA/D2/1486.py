
# %%
from itertools import combinations


T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    min_height = float('inf')
    for i in range(1, N+1):
        for comb in combinations(H, i):
            h_sum = sum(comb)
            if h_sum >= B:
                min_height = min(min_height, h_sum - B)
            
    print(f'#{t+1} {min_height}')
# %%
