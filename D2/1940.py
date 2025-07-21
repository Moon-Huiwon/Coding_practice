#%%
T = int(input())

for t in range(T):
    N = int(input())

    answer = 0
    total_acceleration = 0
    for _ in range(N):
        input_list = list(map(int, input().split()))

        if len(input_list) > 1:
            case_num = input_list[0]
            acceleration = input_list[1]
        else:
            case_num = input_list[0]
        if case_num == 0:
            answer += total_acceleration
        elif case_num == 1:
            total_acceleration += acceleration
            answer += total_acceleration
        else:
            total_acceleration -= acceleration
            if total_acceleration < 0:
                total_acceleration = 0
            answer += total_acceleration

    print(f'#{t+1} {answer}')


# %%
