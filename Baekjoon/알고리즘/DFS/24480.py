import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**7)

def dfs(start_node):
    global cnt
    visited[start_node] = cnt

    for node in adj[start_node]:
        if visited[node] != 0:
            continue
        
        cnt += 1
        dfs(node)
        
N, M, R = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(N+1):
    adj[i].sort(reverse=True)

visited = [0]*(N+1)
cnt = 1
dfs(R)

for i in range(1,N+1):
    print(visited[i])