from collections import deque

def bfs(cal_num, cnt):    
    q = deque([[cal_num, cnt]]) # q에 저장
    visited = set([cal_num]) # 중복 계산을 방지하기 위해 계산된 숫자 저장
    
    while q:
        num, cnt = q.popleft() # 숫자와 계산 횟수 가져오기

        if num == M: # M 자연수 만들었으면 cnt 도출
            return cnt
        
        for next_num in [num+1, num-1, num*2, num-10]: # 다음 숫자 전부 실행
            if 0 < next_num <= 1000000 and next_num not in visited: # 숫자는 백만 이하의 자연수이고, 계산된 적이 없는 숫자여야함
                q.append([next_num, cnt+1]) # 계산된 숫자와 계산 횟수 저장
                visited.add(next_num) # 계산된 숫자 저장

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    cnt = bfs(N, 0)
    print(f'#{t+1} {cnt}')