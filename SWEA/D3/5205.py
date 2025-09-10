import sys
sys.stdin = open('input.txt')

def hoare_partition(left, right):
    mid = (left + right) // 2
    pivot = A[mid] # pivot 설정
    A[left], A[mid] = A[mid], A[left] # pivot 왼쪽으로 이동
    
    i = left + 1
    j = right

    while i <= j:
        while i <= j and A[i] <= pivot: # i는 pivot보다 큰 값 찾을 때 까지 이동
            i += 1
        while i <= j and A[j] >= pivot: # j는 pivot보다 작은 값 찾을 때 까지 이동
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i] # 서로 위치 바꿔주기

    A[left], A[j] = A[j], A[left]

    return j

def quick_sort(left, right):
    if left < right:
        standard = hoare_partition(left, right)

        quick_sort(left, standard-1) # standard을 기준으로 왼쪽 정렬
        quick_sort(standard+1, right) # standard을 기준으로 오른쪽 정렬

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(0, N-1)
    print(f'#{t+1} {A[N//2]}')