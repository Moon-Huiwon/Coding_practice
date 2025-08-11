def check_palindrome(row, col, index_list):
    global row_cnt, col_cnt
    answer = 0
    while index_list:
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
    
    if row_cnt == length // 2:
        answer += 1
    if col_cnt == length // 2:
        answer += 1
    
    return answer

for _ in range(10):
    # 테스트 케이스 숫자 받기
    t = int(input())

    # 100*100 글자판 생성
    table = [list(char for char in input()) for _ in range(100)]
    
    # for문에서 벗어나기 위한 설정(break 기능)
    flag = False

    # 가장 긴 회문을 찾아야하기 때문에 100부터 순차적으로 줄어들게 설정
    for length in range(100,0,-1):
        for i in range(100):
            for j in range(100):
                # index_list를 활용해서 양쪽 값이 같은지 확인
                index_list = [i for i in range(length)]
                
                # 가로 회문 확인하는 변수
                row_cnt = 0
                # 세로 회문 확인하는 변수
                col_cnt = 0
                
                # 회문의 길이가 짝수일때
                if length % 2 == 0:
                    # 양쪽 끝 값 전부 확인하는 코드
                    answer = check_palindrome(i, j, index_list)
                # 홀수일때
                else:
                    # 회문을 판단할 때 필요없는 가운데 index값 제거
                    index_list.remove(length // 2)
                    
                    # 양쪽 끝 값 전부 확인하는 코드
                    answer = check_palindrome(i, j, index_list)
                
                # answer > 0 이면 회문을 찾은 것
                if answer > 0:
                    flag = True
                    break
            
            # for문 안돌아가게 설정
            if flag:
                break
        
        # for문 안돌아가게 설정
        if flag:
            break

    print(f'#{t} {length}')

# %%
