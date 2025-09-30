import sys
sys.setrecursionlimit(10**5)

def dfs(row, col):
    
    global ans

    if row >= N or col >= N:
        return

    num = game_map[row][col]
    if num == -1:
        ans = 'HaruHaru'
        return

    if visited[row][col] == 1:
        return
    
    visited[row][col] = 1

    for dx, dy in [(0,1), (1,0)]:
        nx, ny = row + dx*num, col + dy*num
        dfs(nx, ny)
    
    visited[row][col] = 0

        
N = int(input())
game_map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
ans = 'Hing'
dfs(0,0)
print(ans)