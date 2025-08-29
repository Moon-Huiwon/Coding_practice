T = int(input())

for t in range(T):
    N, M, L = map(int, input().split())

    nodes = [0] * (N+1)
    for _ in range(M):
        par, child = map(int, input().split()) #부모/자식 노드
        nodes[par] = child # 부모 노드에 자식 노드 입력

    for i in range(N, 1, -1): # 리프 노드부터 확인하기 위해 거꾸로
        nodes[i//2] += nodes[i] # 부모 노드에 자식 노드 숫자 더해주기

    print(f'#{t+1} {nodes[L]}')