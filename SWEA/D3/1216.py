
#%%
def repeat(row, col, index_list):
    global row_cnt, col_cnt
    front_idx = index_list.pop(0)
    back_idx = index_list.pop()
    if 0 <= col+front_idx < 100 \
        and 0 <= col+back_idx < 100 \
            and (table[row][col+front_idx] == table[row][col+back_idx]):
        row_cnt += 1
    
    if 0<= row+front_idx < 100 \
        and 0<= row+back_idx < 100 \
            and (table[row+front_idx][col] == table[row+back_idx][col]):
        col_cnt += 1


for _ in range(10):
    t = int(input())
    table = [list(char for char in input()) for _ in range(100)]
    answer = 0
    flag = False
    for length in range(100,0,-1):
        for i in range(100):
            for j in range(100):
                index_list = [i for i in range(length)]
                row_cnt = 0
                col_cnt = 0
                # 짝수일때
                if length % 2 == 0:
                    while index_list:
                        repeat(i, j, index_list)
                    if row_cnt == length // 2:
                        answer += 1
                    if col_cnt == length // 2:
                        answer += 1
                # 홀수일때
                else:
                    index_list.remove(length // 2)
                    while index_list:
                        repeat(i, j, index_list)
                    if row_cnt == length // 2:
                        answer += 1
                    if col_cnt == length // 2:
                        answer += 1
                
                if answer >= 1:
                    flag = True
                    break
                
            if flag:
                break
        
        if flag:
            break

    print(f'#{t} {length}')

# %%
