#%%

T = int(input())
for _ in range(T):
    input()
    use_kneading = list(map(int, input().split()))
    use_topping  = list(map(int, input().split()))

    kneading = [8, 8, 4, 1, 9]
    kneading = [x/16 for x in kneading]
    topping = [1, 30, 25, 10]


    kneading_cnt = []
    for i in range(len(kneading)):
        kneading_cnt.append(use_kneading[i] // kneading[i])
    
    topping_cnt = []
    for i in range(len(topping)):
        topping_cnt.append(use_topping[i] // topping[i])
    
    total_kneading_cnt = min(kneading_cnt)
    total_toppping_cnt = sum(topping_cnt)

    print(int(min(total_kneading_cnt, total_toppping_cnt)))
# %%
