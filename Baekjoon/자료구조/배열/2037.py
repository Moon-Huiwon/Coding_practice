#%%
p, w = map(int, input().split())
message = input()

string_list = [' ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
num_list = []
idx_list = []

for s in message:
    for string in string_list:
        if s in string:
            num_list.append(string_list.index(string))
            idx_list.append(string.index(s))

answer = 0
before_num = 100
for num in num_list:
    if (before_num == num) and num != 0:
        answer += w+p
    else:
        answer += p

    before_num = num

for idx in idx_list:
    answer += idx*p

print(answer)

