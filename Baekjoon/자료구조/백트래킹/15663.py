import sys
input = sys.stdin.readline

def backtracking(lst):
    if len(lst) == M:
        result.add(tuple(lst))
        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(lst+[nums[i]])
            visited[i] = 0

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = set()
visited = [0]*N
backtracking([])

for ans in sorted(result):
    print(*ans)