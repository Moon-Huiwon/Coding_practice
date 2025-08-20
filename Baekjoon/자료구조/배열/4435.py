#%%
gandalf = [1, 2, 3, 3, 4, 10]
sauron = [1, 2, 2, 2, 3, 5, 10]

a = [1, 2]
b = [3, 4]

T = int(input())
for t in range(T):
    gandalf_num = list(map(int, input().split()))
    sauron_num = list(map(int, input().split()))
    
    gandalf_score = [score*num for score, num in zip(gandalf, gandalf_num)]
    sauron_score = [score*num for score, num in zip(sauron, sauron_num)]
    
    if sum(gandalf_score) > sum(sauron_score):
        print(f'Battle {t+1}: Good triumphs over Evil')
    elif sum(gandalf_score) < sum(sauron_score):
        print(f'Battle {t+1}: Evil eradicates all trace of Good')
    else:
        print(f'Battle {t+1}: No victor on this battle field')
# %%
1 