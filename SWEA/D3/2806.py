import sys
sys.stdin = open('input.txt')

def n_queen(row):
    global ans

    if row == N: # 종료조건
        ans += 1
        return
    
    for col in range(N):
        valid = True
        for prev_row in range(row):
            # 같은 열 or 대각선에 있는 경우
            if visited[prev_row] == col or abs(visited[prev_row] - col) == abs(prev_row - row):
                valid = False
                break
        if valid:
            visited[row] = col
            n_queen(row + 1)
            
T = int(input())
for t in range(T):
    N = int(input())
    ans = 0
    visited = [0]*N
    n_queen(0)
    print(f'#{t+1} {ans}')