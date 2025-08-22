def dfs(node):
    global cnt
    
    visited[node] = 1
    cnt += 1

    if len(adj[node]) == 0: # 자식 노드가 없으면 서브트리 끝
        return

    for child_node in adj[node]: # 자식노드 끝까지 확인
        if visited[child_node] == 0:
            dfs(child_node)

T = int(input())
for t in range(T):
    E, N = map(int, input().split())

    adj = [[] for _ in range(E+2)]
    connect_node = list(map(int, input().split()))
    for i in range(0, len(connect_node), 2):
        adj[connect_node[i]].append(connect_node[i+1]) # 단방향
    
    visited = [0]*(E+2)
    cnt = 0
    
    dfs(N)
    
    print(f'#{t+1} {cnt}')
