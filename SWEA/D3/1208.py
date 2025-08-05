#%%
for t in range(10):
    dump_cnt = int(input())
    height = list(map(int, input().split()))

    for _ in range(dump_cnt):
        max_height = max(height)
        max_index = height.index(max_height)
        height[max_index] = max_height - 1

        min_height = min(height)
        min_index = height.index(min_height)
        height[min_index] = min_height + 1

        # 제약조건에 의해
        if max_height - min_height <= 1:
            break
        else:
            continue

    print(f'#{t+1} {max(height) - min(height)}')
# %%
