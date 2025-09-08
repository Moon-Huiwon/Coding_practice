def backtracking(start, lst):
    if len(lst) == M:
        result.append(lst)
        return

    for i in range(start, N):
        backtracking(i+1, lst + [nums[i]])

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []
backtracking(0, [])
for i in range(len(result)):
    print(*result[i])