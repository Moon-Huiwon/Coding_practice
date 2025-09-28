def dfs(start_node):
    
    if dfs_visited[start_node] == 0:
        dfs_result.append(start_node)
        dfs_visited[start_node] = 1
    
    for nodes in arr[start_node]:
        if dfs_visited[nodes] == 0:
            dfs(nodes)


from collections import deque
def bfs(start_node):
    
    q = deque([start_node])
    while q:
        
        node = q.popleft()
        
        if bfs_visited[node] == 0:
            bfs_result.append(node)
            bfs_visited[node] = 1
        
        for nodes in arr[node]:
            if bfs_visited[nodes] == 0:
                q.append(nodes)



N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)
    
for i in range(N+1):
    arr[i].sort()

dfs_visited = [0]*(N+1)
dfs_result = []
dfs(V)
print(*dfs_result)

bfs_visited = [0]*(N+1)
bfs_result = []
bfs(V)
print(*bfs_result)
