#%%
cnt_list = [0] * 26
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
S = [char for char in input()]

for char in S:
    idx = alphabet.index(char)
    cnt_list[idx] += 1

print(*cnt_list)

# %%
