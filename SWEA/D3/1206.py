#%%
for t in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))

    answer = 0
    for i in range(2, N-2):
        building_num = []
        
        if buildings[i] - buildings[i-1] > 0:
            building_num.append(buildings[i] - buildings[i-1])
        else:
            building_num.append(0)
        if buildings[i] - buildings[i-2] > 0:
            building_num.append(buildings[i] - buildings[i-2])
        else:
            building_num.append(0)
        if buildings[i] - buildings[i+1] > 0:
            building_num.append(buildings[i] - buildings[i+1])
        else:
            building_num.append(0)
        if buildings[i] - buildings[i+2] > 0:
            building_num.append(buildings[i] - buildings[i+2])
        else:
            building_num.append(0)

        answer += min(building_num)
    
    print(f'#{t+1} {answer}')
# %%
