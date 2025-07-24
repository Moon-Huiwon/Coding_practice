#%%
T = int(input())

for _ in range(T):
    case_num, case_length = map(str, input().split())
    numbers = list(map(str, input().split()))

    eng_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_dict = {}

    for idx, eng in enumerate(eng_num):
        num_dict[eng] = idx

    change_numbers = [num_dict[num] for num in numbers]
    change_numbers.sort()

    reversed_num_dict = {v: k for k, v in num_dict.items()}

    answer = [reversed_num_dict[num] for num in change_numbers]

    print(f'{case_num}')
    print(*answer)