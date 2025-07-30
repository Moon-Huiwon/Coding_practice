#%%
T = int(input())
    
for t in range(T):
    cards, change_cnt = map(int, input().split())
    cards_list = [int(char) for char in str(cards)]

    optimal = sorted(cards_list, reverse= True)

    cnt = 0
    while cnt < change_cnt:
        if cards_list == optimal:
            while cnt < change_cnt:
                change_num = cards_list[-1]
                cards_list[-1] = cards_list[-2]
                cards_list[-2] = change_num
                cnt += 1
        
        else:
            for i in range(change_cnt):
                
                if cards_list == optimal:
                    while cnt < change_cnt:
                        change_num = cards_list[-1]
                        cards_list[-1] = cards_list[-2]
                        cards_list[-2] = change_num
                        cnt += 1 

                else:
                    max_num = max(cards_list[i:])
                    
                    idx_list = [j for j in range(len(cards_list))][i:]
                    
                    max_num_idx = []
                    
                    for idx, num in enumerate(cards_list):
                        if num == max_num:
                            max_num_idx.append(idx)
                    
                    remain = list(set(idx_list) - set(max_num_idx))
                    use_remain = remain[:len(max_num_idx)]
                    
                    if len(use_remain) > 1:
                        small_num = []
                        for k in range(len(use_remain)):
                            small_num.append(cards_list[use_remain[k]])
                        small_num.sort()
                        
                        idx_num = -1
                        for r in range(len(use_remain)):
                            if cnt < change_cnt:
                                change_num = cards_list[cards_list.index(small_num[r])]
                                cards_list[cards_list.index(small_num[r])] = cards_list[max_num_idx[idx_num]]
                                cards_list[max_num_idx[idx_num]] = change_num

                                cnt += 1
                                idx_num -= 1
                            else:
                                break

                    else:

                        if cards_list == optimal:
                            while cnt < change_cnt:
                                change_num = cards_list[-1]
                                cards_list[-1] = cards_list[-2]
                                cards_list[-2] = change_num
                                cnt += 1 

                        else:
                        
                            change_num = cards_list[use_remain[0]]
                            cards_list[use_remain[0]] = cards_list[max_num_idx[0]]
                            cards_list[max_num_idx[0]] = change_num

                            cnt += 1


    print(f'#{t+1} {"".join(map(str, cards_list))}')


#%%
# CASE 2
T = int(input())
    
def repeat():
    global cards_list, cnt, change_cnt
    
    while cnt < change_cnt:
        if len(cards_list) == len(set(cards_list)):
            # cards_list[-1], cards_list[-2] = cards_list[-2], cards_list[-1]
            change_num = cards_list[-1]
            cards_list[-1] = cards_list[-2]
            cards_list[-2] = change_num
            cnt +=1
        else:
            cnt += 1
            

for t in range(T):
    cards, change_cnt = map(int, input().split())
    cards_list = [int(char) for char in str(cards)]

    optimal = sorted(cards_list, reverse= True)

    cnt = 0
    
    if cards_list == optimal:
        repeat()
    
    else:
        for i in range(len(cards_list)):
            
            if cnt >= change_cnt:
                break

            if cards_list == optimal:
                repeat()

            elif (cards_list != optimal) and (cnt < change_cnt):
                max_num = max(cards_list[i:])
                
                idx_list = [j for j in range(len(cards_list))][i:]
                
                max_num_idx = []
                
                for idx, num in enumerate(cards_list):
                    if num == max_num:
                        max_num_idx.append(idx)
                
                remain = list(set(idx_list) - set(max_num_idx))
                use_remain = remain[:len(max_num_idx)]
                
                if len(use_remain) > 1:
                    small_num = []
                    for k in range(len(use_remain)):
                        small_num.append(cards_list[use_remain[k]])
                    small_num.sort()
                    
                    idx_num = -1
                    for r in range(len(use_remain)):
                        if cnt < change_cnt:
                            # cards_list[cards_list.index(small_num[r])], cards_list[max_num_idx[idx_num]] = cards_list[max_num_idx[idx_num]], cards_list[max_num_idx[idx_num]]
                            change_num = cards_list[cards_list.index(small_num[r])]
                            cards_list[cards_list.index(small_num[r])] = cards_list[max_num_idx[idx_num]]
                            cards_list[max_num_idx[idx_num]] = change_num

                            cnt += 1
                            idx_num -= 1
                        else:
                            break
                
                
                elif max_num == cards_list[i:][0]:
                    continue

                else:
                    # cards_list[use_remain[0]], cards_list[max_num_idx[0]] = cards_list[max_num_idx[0]], cards_list[use_remain[0]]
                    change_num = cards_list[use_remain[0]]
                    cards_list[use_remain[0]] = cards_list[max_num_idx[-1]]
                    cards_list[max_num_idx[-1]] = change_num
                    cnt += 1

            else:
                break

    print(f'#{t+1} {"".join(map(str, cards_list))}')


# %%


# %%
