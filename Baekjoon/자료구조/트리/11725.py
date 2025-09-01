import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**7)

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    node1, node2 = map(int, input().split())
    arr[node1].append(node2)
    arr[node2].append(node1)

visited = [0]*(N+1)

def dfs(node): 
    for i in arr[node]:
        if visited[i] == 0:
            visited[i] = node
            dfs(i)

dfs(1)
for i in range(2, N+1):
    print(visited[i])