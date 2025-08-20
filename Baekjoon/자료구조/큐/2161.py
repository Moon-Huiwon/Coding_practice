N = int(input())

nums = [i for i in range(N, 0, -1)]
stack = []
while len(nums) > 1:
    stack.append(nums.pop())
    num = nums.pop()
    nums = [num] + nums

stack.append(nums[0])
print(*stack)
