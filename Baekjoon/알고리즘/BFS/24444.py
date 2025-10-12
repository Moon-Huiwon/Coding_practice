from collections import deque
import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

def bfs(node):
    global cnt
    q = deque([node])
    visited[node] = 1
    
    while q:
        current_node = q.popleft()
        
        for next_node in adj[current_node]:
            if visited[next_node] == 0:
                cnt += 1
                visited[next_node] = cnt
                q.append(next_node)

N, M, R = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N+1):
    adj[i].sort()

cnt = 1
visited = [0] * (N+1)
bfs(R)

for i in range(1, N+1):
    print(visited[i])