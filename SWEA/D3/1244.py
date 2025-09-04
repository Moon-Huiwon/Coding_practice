# #%%
# T = int(input())
    
# for t in range(T):
#     cards, change_cnt = map(int, input().split())
#     cards_list = [int(char) for char in str(cards)]

#     optimal = sorted(cards_list, reverse= True)

#     cnt = 0
#     while cnt < change_cnt:
#         if cards_list == optimal:
#             while cnt < change_cnt:
#                 change_num = cards_list[-1]
#                 cards_list[-1] = cards_list[-2]
#                 cards_list[-2] = change_num
#                 cnt += 1
        
#         else:
#             for i in range(change_cnt):
                
#                 if cards_list == optimal:
#                     while cnt < change_cnt:
#                         change_num = cards_list[-1]
#                         cards_list[-1] = cards_list[-2]
#                         cards_list[-2] = change_num
#                         cnt += 1 

#                 else:
#                     max_num = max(cards_list[i:])
                    
#                     idx_list = [j for j in range(len(cards_list))][i:]
                    
#                     max_num_idx = []
                    
#                     for idx, num in enumerate(cards_list):
#                         if num == max_num:
#                             max_num_idx.append(idx)
                    
#                     remain = list(set(idx_list) - set(max_num_idx))
#                     use_remain = remain[:len(max_num_idx)]
                    
#                     if len(use_remain) > 1:
#                         small_num = []
#                         for k in range(len(use_remain)):
#                             small_num.append(cards_list[use_remain[k]])
#                         small_num.sort()
                        
#                         idx_num = -1
#                         for r in range(len(use_remain)):
#                             if cnt < change_cnt:
#                                 change_num = cards_list[cards_list.index(small_num[r])]
#                                 cards_list[cards_list.index(small_num[r])] = cards_list[max_num_idx[idx_num]]
#                                 cards_list[max_num_idx[idx_num]] = change_num

#                                 cnt += 1
#                                 idx_num -= 1
#                             else:
#                                 break

#                     else:

#                         if cards_list == optimal:
#                             while cnt < change_cnt:
#                                 change_num = cards_list[-1]
#                                 cards_list[-1] = cards_list[-2]
#                                 cards_list[-2] = change_num
#                                 cnt += 1 

#                         else:
                        
#                             change_num = cards_list[use_remain[0]]
#                             cards_list[use_remain[0]] = cards_list[max_num_idx[0]]
#                             cards_list[max_num_idx[0]] = change_num

#                             cnt += 1


#     print(f'#{t+1} {"".join(map(str, cards_list))}')


# #%%
# CASE 2
# T = int(input())
    
# def repeat():
#     global cards_list, cnt, change_cnt
    
#     while cnt < change_cnt:
#         if len(cards_list) == len(set(cards_list)):
#             # cards_list[-1], cards_list[-2] = cards_list[-2], cards_list[-1]
#             change_num = cards_list[-1]
#             cards_list[-1] = cards_list[-2]
#             cards_list[-2] = change_num
#             cnt +=1
#         else:
#             cnt += 1
            

# for t in range(T):
#     cards, change_cnt = map(int, input().split())
#     cards_list = [int(char) for char in str(cards)]

#     optimal = sorted(cards_list, reverse= True)

#     cnt = 0
    
#     if cards_list == optimal:
#         repeat()
    
#     else:
#         for i in range(len(cards_list)):
            
#             if cnt >= change_cnt:
#                 break

#             if cards_list == optimal:
#                 repeat()

#             elif (cards_list != optimal) and (cnt < change_cnt):
#                 max_num = max(cards_list[i:])
                
#                 idx_list = [j for j in range(len(cards_list))][i:]
                
#                 max_num_idx = []
                
#                 for idx, num in enumerate(cards_list):
#                     if num == max_num:
#                         max_num_idx.append(idx)
                
#                 remain = list(set(idx_list) - set(max_num_idx))
#                 use_remain = remain[:len(max_num_idx)]
                
#                 if len(use_remain) > 1:
#                     small_num = []
#                     for k in range(len(use_remain)):
#                         small_num.append(cards_list[use_remain[k]])
#                     small_num.sort()
                    
#                     idx_num = -1
#                     for r in range(len(use_remain)):
#                         if cnt < change_cnt:
#                             # cards_list[cards_list.index(small_num[r])], cards_list[max_num_idx[idx_num]] = cards_list[max_num_idx[idx_num]], cards_list[max_num_idx[idx_num]]
#                             change_num = cards_list[cards_list.index(small_num[r])]
#                             cards_list[cards_list.index(small_num[r])] = cards_list[max_num_idx[idx_num]]
#                             cards_list[max_num_idx[idx_num]] = change_num

#                             cnt += 1
#                             idx_num -= 1
#                         else:
#                             break
                
                
#                 elif max_num == cards_list[i:][0]:
#                     continue

#                 else:
#                     # cards_list[use_remain[0]], cards_list[max_num_idx[0]] = cards_list[max_num_idx[0]], cards_list[use_remain[0]]
#                     change_num = cards_list[use_remain[0]]
#                     cards_list[use_remain[0]] = cards_list[max_num_idx[-1]]
#                     cards_list[max_num_idx[-1]] = change_num
#                     cnt += 1

#             else:
#                 break

#     print(f'#{t+1} {"".join(map(str, cards_list))}')


# %%
# input 정보 숫자의 자릿수가 커지면 잘못된 결과를 출력함,,, (테케는 전부 통과)
"""
1
843882177 3
"""
import sys
sys.stdin = open('input.txt')

def change_rule(start, cnt):

    if cnt == change_cnt: # 종료조건
        return
    # card가 최적의 card 값이고, 남은 교환 횟수가 짝수 이거나 중복된 숫자가 있으면 종료(어차피 결과는 최적의 card로 나옴)
    if cards == optimal_cards and ((change_cnt - cnt) % 2 == 0 or len(set(cards)) != len(cards)):
        return
    # card가 최적인 card 값이고, 남은 교환 횟수가 홀수이고, 중복된 숫자가 없으면 마지막 2개 숫자 교환하고 종료
    if cards == optimal_cards and (change_cnt - cnt) % 2 == 1 and len(set(cards)) == len(cards):
        cards[-1], cards[-2] = cards[-2], cards[-1]
        return

    max_value = max(cards[start:]) # 최대 값 찾기
    max_idx = ''.join(cards).rfind(max_value) # 최대값 index 확인
    
    if cards[start:].count(max_value) == 1 or change_cnt - cnt == 1: # 최대값의 개수가 하나이거나 교환 횟수가 하나일때
        if cards[start] != max_value: #start에 있는 값이 max_value가 아니면
            cards[start], cards[max_idx] = cards[max_idx], cards[start] # 교환 진행
            change_rule(start+1, cnt+1) # start index / cnt 증가
        else:
            change_rule(start+1, cnt) # start index 증가 / cnt는 동일
    else: # 최대값의 개수가 두개 이상이고, 교환횟수가 두개 이상일 때
        tmp = [] # max 값보다 작은 값 저장
        for value in cards[start:]: 
            if value < max_value:
                tmp.append(value)
        
        # 교환할 숫자 카드 저장 (남은 교환횟수와 최대값 개수 중 작은 값 만큼만 숫자 카드 저장)
        chg_list = tmp[:min(change_cnt - cnt, cards[start:].count(max_value))]
        chg_list.sort() # 오른차순으로 정리 (작은 값을 뒤에 있는 숫자 카드와 교환하게 하기 위해서)

        chg_index_list = []
        for chg_value in chg_list:
            max_idx = ''.join(cards).rfind(max_value) # 최대값 index
            chg_idx = ''.join(cards).find(chg_value) # 바꿀 값 index
            chg_index_list.append(chg_idx)
            cards[chg_idx], cards[max_idx] = cards[max_idx], cards[chg_idx] # 교환하기
       
        change_rule(max(chg_index_list), cnt+len(chg_list))


T = int(input())
for t in range(T):
    cards, change_cnt = map(int, input().split())
    cards = [char for char in str(cards)]
    optimal_cards = sorted(cards, reverse=True)

    change_rule(0,0)
    print(f'#{t+1} {"".join(cards)}')

# %%
def dfs(cnt):
    global ans

    if cnt == change_cnt:
        ans = max(ans, int(''.join(cards)))
        return
    
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            cards[i], cards[j] = cards[j], cards[i]

            check_card = int(''.join(cards))

            if (cnt, check_card) not in visited:
                visited.append((cnt, check_card))
                dfs(cnt+1)
            
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())
for t in range(T):
    cards, change_cnt = map(int, input().split())
    cards = list(str(cards))
    optimal_cards = sorted(cards, reverse=True)
    visited = []
    ans = 0
    dfs(0)

    print(f'#{t+1} {ans}')