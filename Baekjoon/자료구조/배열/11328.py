#%%
T = int(input())
for _ in range(T):
    cnt_str1 = [0] * 26
    cnt_str2 = [0] * 26
    str1, str2 = map(str, input().split())

    for s in str1:
        idx = ord(s) - 97
        cnt_str1[idx] += 1

    for s in str2:
        idx = ord(s) - 97
        cnt_str2[idx] += 1

    if cnt_str1 == cnt_str2:
        print('Possible')
    else:
        print('Impossible')