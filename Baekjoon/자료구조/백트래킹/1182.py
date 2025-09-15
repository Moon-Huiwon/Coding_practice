import sys
input = sys.stdin.readline

def backtracking(start, sum_value):
    global cnt

    if start >= N: # 전부 탐색 완료
        if sum_value == S: # 값을 찾았으면
            cnt += 1 # 개수 업데이트
        return
    
    backtracking(start+1, sum_value+nums[start]) # 현재 위치의 숫자 더해주기
    backtracking(start+1, sum_value) # 현재 위치의 숫자 패스
        
N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
backtracking(0,0)

if S == 0: 
    cnt -= 1 # 공집합 제거해주기
    
print(cnt)