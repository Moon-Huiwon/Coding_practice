#%%
T = int(input())
for _ in range(T):
    test_num = int(input())
    scores = list(map(int, input().split()))

    dict = {}
    for num in scores:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    most_cnt = 0
    max_score = 0

    for score, cnt in dict.items():
        if (cnt > most_cnt) or (cnt == most_cnt and score > max_score):
            most_cnt = cnt
            max_score = score

    print(f'#{test_num} {max_score}')