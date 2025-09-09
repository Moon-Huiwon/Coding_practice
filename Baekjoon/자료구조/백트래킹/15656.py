def backtracking(lst):

    if len(lst) == M:
        result.append(lst)
        return

    for i in range(N):
        backtracking(lst + [nums[i]])

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []

backtracking([])
for i in range(len(result)):
    print(*result[i])