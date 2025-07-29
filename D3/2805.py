#%%
T = int(input())
for t in range(T):
    N = int(input())
    table = list([int(char) for char in input()] for _ in range(N))

    center = N // 2

    answer = 0
    index_num = [i for i in range(center)]
    for row in range(N):
        if row <= center:
            answer += sum(table[row][center-row:center+row+1])
            
        else:
            i = index_num.pop()
            answer += sum(table[row][center-i:center+i+1])
            
    
    print(f'#{t+1} {answer}')    