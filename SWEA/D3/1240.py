T = int(input())

code_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9

}

for t in range(T):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]

    def start_row():
        for i in range(N):
            if arr[i] == '0'*M:
                continue
            else:
                break
        return i

    i = start_row()

    tmp = arr[i][::-1]
    
    j = 0
    while (j < M) and (tmp[j]) == '0':
        j += 1

    value_list = []
    while j + 7 < M:
        
        code_segment = tmp[j:j+7][::-1]
        if code_segment == '0'*7:
            break
        if code_segment in code_dict:
            value_list.append(code_dict[code_segment])
            j += 7
    
    value_list = value_list[::-1]


    odd = 0
    for k in range(0, len(value_list), 2):
        odd += value_list[k]

    even  = 0
    for k in range(1, len(value_list), 2):
        even += value_list[k]

    if (odd * 3 + even) % 10 == 0:
        print(f'#{t+1} {odd + even}')
    else:
        print(f'#{t+1} {0}')
