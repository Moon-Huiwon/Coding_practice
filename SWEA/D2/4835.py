#%%
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    min_value = float('inf')
    max_value = float('-inf')

    for i in range(N-M+1):
        value = sum(a[i:i+M])
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

    print(f'#{t+1} {max_value - min_value}')