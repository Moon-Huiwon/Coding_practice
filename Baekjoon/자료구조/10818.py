#%%
N = int(input())
num_list = list(map(int, input().split()))

def min_max_find(num_list):
    min_value = float('inf')
    max_value = float('-inf')
    
    for num in num_list:
        if num < min_value:
            min_value = num
        
        if num > max_value:
            max_value = num
    
    return min_value, max_value

min_value, max_value = min_max_find(num_list)
print(min_value, max_value)
# %%
