def bfs(S, G):
    # 방문 여부 확인하기 위한 리스트
    visited = [0] * (V+1)
    
    # queue 이용
    q = []
    # 출발 노드 넣기
    q.append(S)
    # 출발 노드 방문했으므로 1 입력
    visited[S] = 1
    
    # 방문 가능한 노드를 전부 돌때까지 반복문 작동
    while q:
        # 방문할 노드 (선입선출 방식)
        node = q.pop(0)

        # 현재 노드가 도착 노드와 동일하면 정답 도출
        if node == G:
            # 정답은 엣지의 개수이므로 방문한 노드의 개수 - 1
            return visited[node] - 1

        # 현재 노드에 연결되어있는 노드들 탐색하도록 하는 for문
        for connect_node in adj[node]:
            # 방문을 하지 않았을 때만 방문 가능
            if visited[connect_node] == 0:
                # 방문 가능한 노드 리스트에 넣기
                q.append(connect_node)
                # 부모 노드 + 1 (현재 노드가 몇번째 방문한 노드인지)
                visited[connect_node] = visited[node] + 1
    
    # 불가능하면 0 도출
    return 0

T = int(input())
for t in range(T):
    # V: 노드 개수 E: 엣지 개수
    V, E = map(int, input().split())
    # 각 노드에 연결된 노드 저장 (양방향)
    adj = [[] for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, input().split())
        adj[start].append(end)
        adj[end].append(start)
    # 출발노드/도착노드
    S, G = map(int, input().split())

    # 정답 도출
    ans = bfs(S, G)
    print(f'#{t+1} {ans}')
