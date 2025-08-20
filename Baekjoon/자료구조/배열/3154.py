#%%
num_arr = [[4,2], [1,1], [1,2], [1,3],
           [2,1], [2,2], [2,3],
           [3,1], [3,2], [3,3]]
hour, minute = map(int, input().split(':'))

hour_list = [hour]

high_h = hour
while 1:
    high_h += 24
    if high_h >= 100:
        break
    hour_list.append(high_h)

low_h = hour
while 1:
    low_h -= 24
    if low_h < 0:
        break
    hour_list.append(low_h)

hour_list.sort()

minute_list = [minute]

high_m = minute
while 1:
    high_m += 60
    if high_m >= 100:
        break
    minute_list.append(high_m)

low_m = minute
while 1:
    low_m -= 60
    if low_m < 0:
        break
    minute_list.append(low_m)

minute_list.sort()

time_list = []
effort_list = []
for h in hour_list:
    for m in minute_list:
        if h < 10 and m >= 10:
            time_list.append(f'0{h}:{m}')
            num_str = f'0{h}{m}'
        elif h >=10 and m < 10:
            time_list.append(f'{h}:0{m}')
            num_str = f'{h}0{m}'
        elif h < 10 and m < 10:
            time_list.append(f'0{h}:0{m}')
            num_str = f'0{h}0{m}'
        else:
            time_list.append(f'{h}:{m}')
            num_str = f'{h}{m}'
        
        
        total_effort = 0
        for i in range(3):
            str1 = int(num_str[i])
            str2 = int(num_str[i+1])
            
            effort = abs(num_arr[str1][0] - num_arr[str2][0]) + abs(num_arr[str1][1] - num_arr[str2][1])

            total_effort += effort
        
        effort_list.append(total_effort)

min_effort = min(effort_list)
print(time_list[effort_list.index(min_effort)])
# %%
