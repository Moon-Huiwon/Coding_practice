def run_num(n, lst, winner): # run 함수
    global player1_winner, player2_winner
    if (n-2 in lst and n-1 in lst) \
        or (n-1 in lst and n+1 in lst) \
            or (n+1 in lst and n+2 in lst):
        
        if winner == 1:
            player1_winner = True
        else:
            player2_winner = True
        return
    
def triplet(n, lst, winner): # triplet 함수
    global player1_winner, player2_winner
    if lst.count(n) >= 3:
        if winner == 1:
            player1_winner = True
        else:
            player2_winner = True
        return

T = int(input())
for tc in range(T):
    nums = list(map(int, input().split()))
    player1 = [] # player1 숫자카드
    player2 = [] # player2 숫자카드
    player1_winner = False # player1이 이겼는지
    player2_winner = False # player2이 이겼는지

    ans = 0
    for i in range(0,len(nums),2):
        player1.append(nums[i]) # 숫자카드 넣기
        run_num(nums[i], player1, 1) # run 확인
        triplet(nums[i], player1, 1) # triplet 확인
        
        if player1_winner == True: # run 또는 triplet 발생했으면 player1 승리
            break
        
        player2.append(nums[i+1]) # 숫자카드 넣기
        run_num(nums[i+1], player2, 2) # run 확인
        triplet(nums[i+1], player2, 2) # triplet 확인

        if player2_winner == True: # run 또는 triplet 발생했으면 player2 승리
            break

    if player1_winner == player2_winner: # 무승부
        ans = 0
    elif player1_winner == True: # player1 승리
        ans = 1
    elif player2_winner == True: # player2 승리
        ans = 2

    print(f'#{tc+1} {ans}')
