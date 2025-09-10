import sys
sys.stdin = open('input.txt')

"""처음시도(세제곱근 활용) 불가능***"""
# def cube_root(num):
#     cube_root_value = num ** (1/3)
#     str(cube_root)

#     if int(cube_root_value) == cube_root_value:
#         return int(cube_root_value)
#     else:
#         return -1

def binary_search(l, r):
    global ans
    
    if l > r:
        return
    
    mid = (l + r) // 2 # 중앙값 찾기
    if mid ** 3 == N: # 세제곱근 발견
        ans = mid
        return
    elif mid ** 3 < N: # 숫자가 더 큰 범위내에서 찾아야하므로 left 숫자 이동
        return binary_search(mid+1, r)
    else: # 숫자가 더 작은 범위 내에서 찾아야하므로 right 숫자 이동
        return binary_search(l, mid-1) 

T = int(input())
for t in range(T):
    N = int(input())
    ans = -1
    binary_search(1,N)
    print(f'#{t+1} {ans}')

