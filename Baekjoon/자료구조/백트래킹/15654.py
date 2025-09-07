N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [0] * (N)
result = []
def backtracking(lst):
    # 종료조건
    if len(lst) == M:
        result.append(lst)
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(lst + [nums[i]])
            visited[i] = 0

backtracking([])

for i in range(len(result)):
    print(*result[i])