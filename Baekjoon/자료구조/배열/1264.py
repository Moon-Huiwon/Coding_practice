#%%
small_string = ['a', 'e', 'i', 'o', 'u']
large_string = [string.upper() for string in small_string]
string_list = small_string + large_string

while True:
    sentence = input()
    if sentence == '#':
        break
    
    answer = 0
    for s in sentence:
        if s in string_list:
            answer += 1
    
    print(answer)
