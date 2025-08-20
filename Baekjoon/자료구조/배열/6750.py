#%%
word = input()
use_letters = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']

answer = True
for s in word:
    if s not in use_letters:
        answer = False
        break

if answer == True:
    print('YES')
else:
    print('NO')
# %%
