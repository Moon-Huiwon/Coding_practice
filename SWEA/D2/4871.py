def dfs(S):
    # 도착 노드를 방문했으면 stop
    if G in stack:
        return
    
    # 현재 방문한 노드 stack에 쌓기
    stack.append(S)
    # 방문 여부 처리
    visited[S] = 1

    # 해당 노드에 연결된 노드들 방문하며 탐색
    for node in adj[S]:
        if visited[node] == 0:
            dfs(node)

T = int(input())
for t in range(T):
    # V: 노드 개수 E: 엣지 개수
    V, E = map(int, input().split())
    
    # 각 노드에 연결되어 있는 노드들 저장
    adj = [[] for _ in range(V+1)] # index가 노드 번호를 뜻함
    # 엣지를 통해 연결된 노드들은 확인
    for _ in range(E):
        # 노드 두개 확인
        start, end = map(int, input().split())
        # 단방향 (start 노드 -> end 노드)
        adj[start].append(end)
    
    # 출발 노드와 도착노드 확인
    S, G = map(int,input().split())
    
    # 중복으로 방문하지 않게 방문 여부 처리하는 리스트
    # 각 index 값이 노드 번호를 뜻한다.
    visited = [0] * (V+1)
    
    # 방문한 노드 stack에 쌓기
    stack = []
    
    # dfs를 통해 깊은 탐색 진행
    dfs(S)

    if G in stack:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')
    
