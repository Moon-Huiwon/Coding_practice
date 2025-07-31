#%%
answer_list = ['D', 'C', 'B', 'A', 'E']
for _ in range(3):
    play_list = list(map(int, input().split()))
    play_value = sum(play_list)
    
    print(answer_list[play_value])