A = [num+1 for num in range(12)]
n = len(A)

T = int(input())
for t in range(T):
    N, K = map(int, input().split())

    # 조건에 해당하는 부분집합 저장할 리스트
    partition_group = []
    for i in range(1 << n):

        # 부분집합 생성하는 리스트
        group = []
        for j in range(n):
            if i & (1 << j):
                group.append(A[j])

        # 생성된 부분집합이 조건을 만족하면 partition_group에 저장
        if len(group) == N and sum(group) == K:
            partition_group.append(group)

    print(f'#{t+1} {len(partition_group)}')

