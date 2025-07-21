#%%
T = int(input())

for t in range(T):
    N = int(input())

    answer_list = []

    num_list = [2, 3, 5, 7, 11]
    for num in num_list:
        
        cnt = 0
        
        while N % num == 0:
            N /= num
            cnt += 1
        else:
            answer_list.append(cnt)
    
    print(f'#{t+1} {" ".join(map(str, answer_list))}')
# %%
