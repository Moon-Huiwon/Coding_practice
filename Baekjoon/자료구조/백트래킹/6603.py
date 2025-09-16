def backtracking(start, lst):

    if len(lst) == 6:
        print(*lst)
        return
    
    for i in range(start, k):
        backtracking(i+1, lst+[nums[i]])

while 1:
    nums = list(map(int, input().split()))
    k = nums.pop(0)

    if k == 0:
        break

    backtracking(0, [])
    print()