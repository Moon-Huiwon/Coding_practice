def cal_distance(cnt, total_distance, current):
    global ans

    if total_distance >= ans: # 가지치기
        return

    if cnt == N: # 정답 도출 (마지막 집까지의 거리 더해주기)
        total_distance += (abs(current[0] - home[0]) + abs(current[1] - home[1]))
        ans = min(ans, total_distance)
        return
    
    for i in range(N): # 고객 집 방문
        if visited[i] == 0: # 방문 안한 곳 방문하기
            visited[i] = 1 # 방문 처리
            cal_distance(cnt+1, \
                         total_distance + abs(current[0] - info_list[i][0]) + abs(current[1] - info_list[i][1]),\
                            info_list[i]) # 재귀호출
            visited[i] = 0 # 방문 초기화 (백트래킹을 위해)

T = int(input())
for t in range(T):
    N = int(input())
    info = list(map(int, input().split())) # 정보 가져오기
    
    info_list = [] # 리스트로 저장
    for i in range(0, len(info), 2):
        info_list.append([info[i], info[i+1]])
    visited = [0]*N # 방문 처리 리스트

    company = info_list.pop(0) # 회사 위치
    home = info_list.pop(0) # 집 위치
    
    ans = float("inf")
    cal_distance(0, 0, company)
    print(f'#{t+1} {ans}')