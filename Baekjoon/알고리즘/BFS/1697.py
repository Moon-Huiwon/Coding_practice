import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

from collections import deque

def bfs(idx):
    global ans
    q = deque([[idx, 0]])
    while q:
        now, time = q.popleft()
        
        if time >= ans:
            continue
        
        if now == K:
            ans = min(ans, time)

        for next in [now-1, now+1, 2*now]:
            if next in visited:
                continue
            if not (0 <= next <= 100000):
                continue
            if next != K:
                visited.add(next)
            q.append([next, time+1])

N, K = map(int, input().split())
visited = set()
visited.add(N)
ans = float("inf")
bfs(N)
print(ans)