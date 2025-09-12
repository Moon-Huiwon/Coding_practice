T = int(input())
for t in range(T):
    info = list(input().split())
    before_robot = info[1] # 맨 처음 로봇 받기
    remain_time = 0 # 남은 시간
    total_time = 0 # 최종 시간
    B_button = 1 # 현재 B의 위치
    O_button = 1 # 현재 O의 위치
    
    for i in range(1, len(info), 2):
        if info[i] == 'B':
            if before_robot == 'B': # 연속으로 B 로봇을 움직일 때
                remain_time += (abs(int(info[i+1]) - B_button) + 1)
            else:
                if abs(int(info[i+1]) - B_button) <= remain_time:
                    total_time += remain_time
                    remain_time = 0
                    remain_time += 1
                else:
                    total_time += remain_time
                    remain_time = (abs(int(info[i+1]) - B_button) - remain_time)
                    remain_time += 1
                
            before_robot = 'B'
            
            B_button = int(info[i+1])
        else:
            if before_robot == 'O':
                remain_time += (abs(int(info[i+1]) - O_button) + 1)
            else:
                if abs(int(info[i+1]) - O_button) <= remain_time:
                    total_time += remain_time
                    remain_time = 0
                    remain_time += 1
                else:
                    total_time += remain_time
                    remain_time = (abs(int(info[i+1]) - O_button) - remain_time)
                    remain_time += 1
                
            before_robot = 'O'
            
            O_button = int(info[i+1])
    
    print(f'#{t+1} {total_time+remain_time}')


#%%
T = int(input())
for t in range(T):
    info = list(input().split())
    before_robot = info[1] # 맨 처음 로봇 받기
    remain_time = 0 # 남은 시간
    total_time = 0 # 최종 시간
    # 각 로봇별 현재 위치
    current = {
        'B': 1,
        'O': 1
    }
    
    for i in range(1, len(info), 2):
        if before_robot == info[i]: # 연속으로 같은 로봇일 때
            remain_time += (abs(int(info[i+1]) - current[info[i]]) + 1) # remain_time에 저장 (버튼 누르는 것까지)
        else: # 다른 로봇일 때
            total_time += remain_time # remain_time을 total_time에 저장
            
            if abs(int(info[i+1]) - current[info[i]]) <= remain_time: # 남아 있는 시간보다 이동 시간이 짧으면
                remain_time = 0 # remain_time 시간 없애기
            else:
                remain_time = (abs(int(info[i+1]) - current[info[i]]) - remain_time) # 남아 있는 시간보다 이동 시간이 더 길면 추가 시간을 remain_time에 저장하기
            
            remain_time += 1 # button 누르는 시간 더해주기
        
        before_robot = info[i] # before_robot 업데이트
        current[info[i]] = int(info[i+1]) # 로봇 현재 위치 업데이트
    
    print(f'#{t+1} {total_time+remain_time}')
