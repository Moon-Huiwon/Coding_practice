import sys
from collections import deque
# sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[b].append(a)
    
def bfs(node):
    q = deque([node])
    visited = [0] * (N+1)
    visited[node] = 1
    while q:
        current_node = q.popleft()
        for next_node in adj[current_node]:
            if not visited[next_node]:
                visited[next_node] = 1
                q.append(next_node)
    
    return sum(visited)

max_cnt = 0
ans = []
for i in range(1,N+1):
    cnt = bfs(i)
    if max_cnt == cnt:
        ans.append(i)
    elif cnt > max_cnt:
        ans = [i]
        max_cnt = cnt

print(*ans)