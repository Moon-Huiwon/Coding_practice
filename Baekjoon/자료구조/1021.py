N, M = map(int, input().split())
pull_num = list(map(int, input().split()))
nums = [i+1 for i in range(N)]

ans = 0
for num in pull_num:
    idx = nums.index(num)
    left = len(nums[:idx])
    right = len(nums[idx:])

    if left <= right:
        while left:
            nums.append(nums.pop(0))
            left -= 1
            ans += 1
    else:
        while right:
            move_num = nums.pop()
            nums = [move_num] + nums
            right -= 1
            ans += 1
    
    nums.pop(0)
            
print(ans)    