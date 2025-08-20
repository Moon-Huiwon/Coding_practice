#%%
pattern_list = ['-', '\\', '(', '@', '?', '>', '&', '%', '/']

while True:
    pattern = input()
    if pattern == '#':
        break

    answer = 0
    eight_multi = 8**(len(pattern)-1)
    for p in pattern:
        value = pattern_list.index(p)
        if value == 8:
            value = -1
        answer += value*eight_multi

        eight_multi //= 8
    
    print(answer)
# %%
