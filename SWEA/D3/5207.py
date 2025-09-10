import sys
sys.stdin = open('input.txt')

def binary_search(l, r, num, lst):
    global cnt
    
    if l > r or (len(lst) > 1 and lst[-1] == lst[-2]): # 찾을 수 없거나 같은 방향으로 찾으면 return
        return 

    mid = (l + r) // 2 # 중앙값
    if A[mid] == num: # 찾으면 cnt +1
        cnt += 1
        return
    elif A[mid] < num: # 오른쪽 범위 탐색
        return binary_search(mid+1, r, num, lst + ['right'])
    else: # 왼쪽 범위 탐색
        return binary_search(l, mid-1, num, lst + ['left'])
    
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort() # 오름차순 정리
    B = list(map(int, input().split()))
    cnt = 0
    for num in B:
        binary_search(0, N-1, num, [])
    print(f'#{t+1} {cnt}')