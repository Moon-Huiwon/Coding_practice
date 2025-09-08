def line(start, lst):
    global ans

    if len(lst) == 2:
        if (lst[0][0] - lst[1][0])*(lst[0][1] - lst[1][1]) > 0:
            return
        else:
            ans += 1
            return
    
    for i in range(start, N):
        line(i+1, lst+[line_list[i]])

T = int(input())
for t in range(T):
    N = int(input())
    line_list = []
    for _ in range(N):
        line_list.append(list(map(int, input().split())))
    ans = 0
    line(0, [])
    print(f'#{t+1} {ans}')