#%%
T = int(input())
for t in range(T):
    N = int(input())
    num_list = [int(num) for num in input()]

    answer = 0
    one_cnt = 0
    for num in num_list:
        if num == 1:
            one_cnt += 1
            if one_cnt > answer:
                answer = one_cnt
        else:
            one_cnt = 0

    print(f'#{t+1} {answer}')      

            



    