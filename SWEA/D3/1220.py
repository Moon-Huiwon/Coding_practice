#%%
# with open('input.txt', 'r') as file:
#     size = int(file.readline())
#     init_table = [list(map(int, file.readline().split())) for _ in range(size)] 

#%%
for t in range(10):
    size = int(input())
    init_table = [list(map(int, input().split())) for _ in range(size)]

    for cy in range(size):
        while True:
            moved = False
            for cx in range(size):
                if init_table[cx][cy] == 1:
                    if (0 <= cx + 1 < size) \
                        and (init_table[cx+1][cy] == 0):
                        init_table[cx][cy] = 0
                        init_table[cx+1][cy] = 1
                        moved = True
                        
                    elif (0 <= cx + 1 < size) \
                        and (init_table[cx+1][cy] == 1):
                        continue
                
                elif init_table[cx][cy] == 2:
                    if (0 <= cx - 1 < size) \
                        and (init_table[cx - 1][cy] == 0):
                        init_table[cx][cy] = 0
                        init_table[cx - 1][cy] = 2
                        moved = True

                    elif (0 <= cx - 1 < size) \
                        and (init_table[cx - 1][cy] == 2):
                        continue

            if not moved:
                break       

    state = 0
    for i in range(size-1):
        for j in range(size):
            if init_table[i][j] == 1 and init_table[i+1][j] == 2:
                state += 1
    
    print(f'#{t+1} {state}')


