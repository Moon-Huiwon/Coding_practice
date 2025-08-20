#%%
T = int(input())

num_alias = [0, 'Yakk', 'Doh', 'Seh', 'Ghar', 'Bang', 'Sheesh']
same_num_alias = [0, 'Habb Yakk', 'Dobara', 'Dousa', 'Dorgy', 'Dabash', 'Dosh']

for t in range(T):
    num1, num2 = map(int, input().split())
    
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    
    if num1 == num2:
        print(f'Case {t+1}: {same_num_alias[num1]}')
    elif max_num == 6 and min_num == 5:
        print(f'Case {t+1}: Sheesh Beesh')
    else:
        print(f'Case {t+1}: {num_alias[max_num]} {num_alias[min_num]}')
    
# %%
