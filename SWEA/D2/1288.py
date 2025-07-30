#%%
T = int(input())
for t in range(T):
        
    N = int(input())
    answer = 1
    num_list = []
    while len(set(num_list)) < 10:
        for char in str(N * answer):
            num_list.append(char)
        
        answer += 1

    print(f'#{t+1} {N * (answer - 1)}')

#%%