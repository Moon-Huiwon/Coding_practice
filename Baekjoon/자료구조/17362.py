#%%
finger_rule = [1, 2, 3, 4, 5, 4, 3, 2]

num = int(input())

print(finger_rule[num % len(finger_rule) - 1 ])
