#%%
for t in range(10):
    # 회문의 길이
    length = int(input())
    # 8*8 글자판
    table = [list(char for char in input()) for _ in range(8)]


    answer = 0
    for i in range(8):
        for j in range(8):
            # 회문의 길이만큼 index_list 생성
            # 회문 여부를 판단하는데 사용 (pop(0)과 pop()을 활용하여 양쪽 값을 확인)
            index_list = [idx for idx in range(length)]
            
            # 가로 회문의 개수
            row_cnt = 0
            # 세로 회문의 개수
            col_cnt = 0
            
            # 회문의 길이가 짝수일때
            if length % 2 == 0:
                while index_list:
                    # 시작지점
                    front_idx = index_list.pop(0)
                    # 끝지점
                    back_idx = index_list.pop()
                    
                    # 시작점과 끝지점이 글자판 안에 있고, 회문이면 row_cnt에 더해주기(가로 회문)
                    if 0 <= j+front_idx < 8 \
                        and 0 <= j+back_idx < 8 \
                            and (table[i][j+front_idx] == table[i][j+back_idx]):
                        row_cnt += 1
                    
                    # 시작점과 끝지점이 글자판 안에 있고, 회문이면 col_cnt에 더해주기(세로 회문)
                    if 0<= i+front_idx < 8 \
                        and 0<= i+back_idx < 8 \
                            and (table[i+front_idx][j] == table[i+back_idx][j]):
                        col_cnt += 1
                
                # 양쪽 끝 값이 동일하면 cnt에 더해지는 방식이기 때문에 
                # row(col)_cnt == length//2 와 같을 때 회문이다.
                if row_cnt == length // 2:
                    answer += 1
                if col_cnt == length // 2:
                    answer += 1
            
            # 회문의 길이가 홀수일때
            else:
                # 가운데 값은 확인할 필요 없으므로 index에서 제거
                index_list.remove(length // 2)
                
                # 양쪽 끝 값을 확인 (length가 짝수일떄와 동일하게 작동)
                while index_list:
                    front_idx = index_list.pop(0)
                    back_idx = index_list.pop()
                    if 0 <= j+front_idx < 8 \
                        and 0 <= j+back_idx < 8 \
                            and (table[i][j+front_idx] == table[i][j+back_idx]):
                        row_cnt += 1
                    
                    if 0<= i+front_idx < 8 \
                        and 0<= i+back_idx < 8 \
                            and (table[i+front_idx][j] == table[i+back_idx][j]):
                        col_cnt += 1
                if row_cnt == length // 2:
                    answer += 1
                if col_cnt == length // 2:
                    answer += 1

    print(f'#{t+1} {answer}')

# %%
def check_palindrome(row, col, index_list):
    global row_cnt, col_cnt, answer
    while index_list:
        front_idx = index_list.pop(0)
        back_idx = index_list.pop()
        if 0 <= col+front_idx < 8 \
            and 0 <= col+back_idx < 8 \
                and (table[row][col+front_idx] == table[row][col+back_idx]):
            row_cnt += 1
        
        if 0<= row+front_idx < 8 \
            and 0<= row+back_idx < 8 \
                and (table[row+front_idx][col] == table[row+back_idx][col]):
            col_cnt += 1
    if row_cnt == length // 2:
        answer += 1
    if col_cnt == length // 2:
        answer += 1

for t in range(10):
    length = int(input())
    table = [list(char for char in input()) for _ in range(8)]

    answer = 0
    for i in range(8):
        for j in range(8):
            index_list = [i for i in range(length)]
            row_cnt = 0
            col_cnt = 0
            # 짝수일때
            if length % 2 == 0:
                check_palindrome(i, j, index_list)
            # 홀수일때
            else:
                index_list.remove(length // 2)
                check_palindrome(i, j, index_list)
                
    print(f'#{t+1} {answer}')