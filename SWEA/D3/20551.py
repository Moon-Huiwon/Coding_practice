T = int(input())
for t in range(T):
    candy = list(map(int, input().split()))
    
    ans = 0
    for i in range(2, 0, -1):
        if candy[-1] < 3 or candy[-2] < 2:
            ans = -1
            break
        
        if candy == sorted(candy) and len(set(candy)) == 3:
            break

        if candy[i] <= candy[i-1]:
            ans += (candy[i-1] - candy[i] + 1)
            candy[i-1] = candy[i] - 1
    
    print(f'#{t+1} {ans}')