def dfs(result):
    global cnt
    
    if sum(result) > num:
        return

    if sum(result) == num:
        cnt += 1
        return

    for n in nums_list:
        dfs(result + [n])


nums_list = [1,2,3]

T = int(input())
for _ in range(T):
    num = int(input())
    cnt = 0
    dfs([])
    print(cnt)

