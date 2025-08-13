T = int(input())
for _ in range(T):
    key = list(input())
    left_key = []
    right_key = []
    for k in key:
        if k not in ['<', '>', '-']:
            left_key.append(k)
        else:
            if len(left_key) > 0 and k == '<':
                tmp = left_key.pop()
                right_key.append(tmp)
            elif len(right_key) > 0 and k == '>':
                tmp = right_key.pop()
                left_key.append(tmp)
            elif len(left_key) > 0 and k == '-':
                left_key.pop()

    ans = left_key + right_key[::-1]
    print(''.join(ans))
