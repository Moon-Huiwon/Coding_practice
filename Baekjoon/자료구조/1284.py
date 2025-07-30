#%%
space_list = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]

while True:
    
    number = input()
    
    answer = 0

    if number == '0':
        break
    
    for num in number:
        answer += space_list[int(num)]

    answer += (len(number) + 1)

    print(answer)