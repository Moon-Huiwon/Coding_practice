T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    heap = [0] * (N+1) # 노드1~N까지 리스트 생성
    for i in range(1,N+1):
        heap[i] = nums[i-1] # 노드에 숫자 넣기
        
        while i//2 >= 1: # 부모 노드 > 자식 노드이면 숫자 교환
            if heap[i//2] != 0 and heap[i//2] > heap[i]:
                heap[i//2], heap[i] = heap[i], heap[i//2]

            i //= 2 # 모든 부모 노드 탐색하기 위해

    ans = 0
    sum_node = N // 2 # 마지막 노드의 부모 노드
    while sum_node >= 1: # 모든 부모 노드 탐색
        ans += heap[sum_node]
        sum_node //= 2

    print(f'#{t+1} {ans}')


#%%
# 강사님 코드 참고 (함수 사용한 방법)
def eng(last):

    c = last
    p = c // 2

    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    heap = [0] * (N+1)
    for i in range(1,N+1):
        heap[i] = nums[i-1]
        
        eng(i)

    ans = 0
    sum_node = N // 2
    while sum_node >= 1:
        ans += heap[sum_node]
        sum_node //= 2

    print(f'#{t+1} {ans}')