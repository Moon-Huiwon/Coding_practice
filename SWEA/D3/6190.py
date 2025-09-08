def find_num(start, lst):
    global ans

    if len(lst) == 2:
        if ans > lst[0]*lst[1]: # 가지치기 조건***
            return
        else:
            num = lst[0]*lst[1] # 곱한 값 구하기
            if str(num) == ''.join(sorted(str(num))): # 단조 증가인수 확인
                ans = max(ans, num) # ans 업데이트
            return

    for i in range(start, N):
        find_num(i+1, lst + [A[i]])

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = -1
    find_num(0,[])
    print(f'#{t+1} {ans}')