#%%
T = int(input())
for t in range(T):
    mon_1, day_1, mon_2, day_2 = map(int, input().split())

    thirty = [4, 6, 9, 11]
    thirty_one = [1, 3, 5, 7, 8, 10, 12]

    answer = day_2 - day_1 + 1
    for i in range(mon_1, mon_2):
        if i in thirty:
            answer += 30
        elif i in thirty_one:
            answer += 31
        else:
            answer += 28

    print(f'#{t+1} {answer}')

# %%
