def backtracking(lst):
    if len(lst) == M:
        result.add(tuple(lst))
        return
    
    for i in range(N):
        backtracking(lst+[nums[i]])

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = set()
backtracking([])
for num in sorted(result):
    print(*num)