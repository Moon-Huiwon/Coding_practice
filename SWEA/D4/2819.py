import sys
sys.stdin = open('input.txt')

def move(x, y, nums):

    if len(nums) == 7: # 종료조건
        if ''.join(nums) in ans:
            return
        else:
            ans.add(''.join(nums))
            return

    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]: # 이동 진행
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            move(nx, ny, nums+[str(arr[nx][ny])])

T = int(input())
for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(4)] # 격자판 생성
    ans = set() # ans 값들 저장
    for i in range(4):
        for j in range(4):
            move(i,j,[str(arr[i][j])])
    
    print(f'#{t+1} {len(ans)}')