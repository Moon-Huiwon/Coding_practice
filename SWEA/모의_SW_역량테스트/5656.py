import copy

# 벽돌이 1 이상이면 영향을 주는 벽돌 찾아서 폭발시키기 힘수
def bfs(x, y, arr):
    q = []
    q.append((x, y, arr[x][y]))
    while q:
        cx, cy, block_num = q.pop(0)
        arr[cx][cy] = 0
        for rn in range(1, block_num):
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = cx + rn*dx, cy + rn*dy
                if 0 <= nx < H and 0 <= ny <W and arr[nx][ny] > 0:
                    q.append((nx, ny, arr[nx][ny]))
                
# 벽돌 떨어트리기 함수
def drop_block(arr):
    for j in range(W):
        for i in range(H-1, 0, -1):
            if arr[i][j] == 0:
                for k in range(i-1, -1, -1):
                    if arr[k][j] > 0:
                        arr[i][j] = arr[k][j]
                        arr[k][j] = 0
                        break

# 정답 도출할 함수
def solve(cnt, arr):
    global ans
    
    if cnt == N: # 중단하고 답 도출하는 조건
        tmp = sum(arr[i][j] > 0 for i in range(H) for j in range(W)) # 블록들 개수 세기
        ans = min(ans, tmp) # 답 업데이트
        return
    
    for j in range(W): # 모든 열들을 순서대로 탐색
        for i in range(H): # 위에서 아래로 탐색
            if arr[i][j] > 0:
                new_arr = copy.deepcopy(arr) # arr배열을 중복으로 사용하기 위해 copy 필수***
                bfs(i, j, new_arr) # 블록 폭발
                drop_block(new_arr) # 벽돌 떨어트리기
                solve(cnt+1, new_arr) # 정답 도출
                break # cnt가 끝났으므로 다음 조합으로로 넘어가서 다시 구하기 위해 break

T = int(input())
for t in range(T):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    ans = float('inf')
    solve(0, arr)
    if ans == float('inf'):
        print(f'#{t+1} {0}')
    else:
        print(f'#{t+1} {ans}')