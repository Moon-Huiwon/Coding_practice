from collections import deque
import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")

def bfs(num):
    q = deque(adj[num])
    while q:
        friend = q.popleft()
        visited[friend] = 1
        for next_friend in adj[friend]:
            if visited[next_friend] == 0:
                visited[next_friend] = 1

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0]*(n+1)
visited[1] = 1
cnt = 0
bfs(1)
print(sum(visited) - 1)