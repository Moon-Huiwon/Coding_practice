def backtracking(start, lst):
    if len(lst) == M:
        result.add(tuple(lst))
        return
    
    for i in range(start, N):
        backtracking(i, lst + [nums[i]])
    
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = set()
backtracking(0,[])

for num in sorted(result):
    print(*num)