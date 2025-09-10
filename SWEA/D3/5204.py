import sys
sys.stdin = open('input.txt')

def merge_sort(nums):
    global cnt
    
    if len(nums) == 1: # 길이가 1이면 더이상 쪼갤 수 없기 때문에 stop
        return nums
    
    mid = len(nums)//2 # mid index 설정
    L = merge_sort(nums[:mid]) # left 리스트 설정
    R = merge_sort(nums[mid:]) # right 리스트 설정

    if L[-1] > R[-1]: # 경우의 수 cnt + 1
        cnt += 1

    sort_nums = [] # 오름차순 정리된 숫자 리스트 넣기
    
    i = 0 # 초기 index
    j = 0 # 초기 index

    while i < len(L) and j < len(R): # 한쪽 리스트를 전부 볼 때까지 서로 비교
        if L[i] < R[j]:
            sort_nums.append(L[i])
            i += 1
        else:
            sort_nums.append(R[j])
            j += 1
    
    # 비교가 끝나고 저장이 안된 남아있는 숫자 리스트에 넣기
    if i != len(L):
        sort_nums += L[i:]
    if j != len(R):
        sort_nums += R[j:]
    
    return sort_nums


T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    sort_nums = merge_sort(nums)
    print(f'#{t+1} {sort_nums[N//2]} {cnt}')