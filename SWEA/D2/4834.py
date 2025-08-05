#%%
T = int(input())
for t in range(T):
    num_cnt = int(input())
    num_list = [int(num) for num in input()]

    num_cnt_list = [0] * 10

    for num in num_list:
        num_cnt_list[num] += 1

    max_cnt = max(num_cnt_list)
    if num_cnt_list.count(max_cnt) > 1:
        max_cnt_num_list = [idx for idx in range(10) if num_cnt_list[idx] == max_cnt]
        max_cnt_num = max_cnt_num_list[-1]
    else:
        max_cnt_num = num_cnt_list.index((max_cnt))

    print((f'#{t+1} {max_cnt_num} {max_cnt}'))