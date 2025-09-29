import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start_node):

    visited[start_node] = 1

    for node in adj[start_node]:
        if visited[node] == 0:
            dfs(node)

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [0]*(N+1)
ans = 0
for i in range(1,N+1):
    if visited[i] == 0:
        dfs(i)
        ans += 1

print(ans)