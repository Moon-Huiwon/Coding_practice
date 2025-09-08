# import sys
# sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    A = [] # 화물 작업 시간 저장
    for _ in range(N):
        s, e = map(int, input().split())
        A.append((e,s)) # 종료 시점/시작 시점
    
    A.sort() # 종료 시점 기준으로 오름차순 정리
    ans = 1
    tmp_lst = []
    while len(A) > 0:
        if len(tmp_lst) == 0: # 시간 비교 대상 없음
            tmp_lst.append(A.pop(0)) # tmp_lst에 가장 빨리 끝나는 작업 넣기
        else:
            if tmp_lst[0][0] <= A[0][1]: # 가장 빨리 끝나는 작업의 종료 시점 <= 그 다음 작업의 시작시점
                tmp_lst.append(A.pop(0)) # 다음 작업 저장
            else:
                A.pop(0) # 불가능한 작업이므로 A에서 제거

        if len(tmp_lst) == 2: # 앞의 작업 종료시 다음 작업 진행할 거 있음
            ans += 1 # 화물차 개수에 더해주기
            tmp_lst.pop(0) # 연속적으로 확인하기 위해 맨 앞 값 제거
    
    print(f'#{tc+1} {ans}')