#%%
word = [char for char in input()]
answer = [char for char in word if char not in 'CAMBRIDGE']

print(''.join(answer))


