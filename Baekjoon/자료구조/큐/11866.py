N, K = map(int, input().split())
nums = [i+1 for i in range(N)]
start_idx = -1
stack = []
while len(nums) > 1:
    if start_idx + K < len(nums):
        stack.append(nums[start_idx + K])
        nums.pop(start_idx + K)
        start_idx += (K - 1)
    else:
        start_idx -= len(nums)
        while start_idx + K >= len(nums):
            start_idx -= len(nums)
        stack.append(nums[start_idx + K])
        nums.pop(start_idx + K)
        start_idx += (K - 1)

stack.append(nums[0])
print('<', end="")
for i in range(len(stack)):
    if i < len(stack)-1:
        print(f'{stack[i]}, ', end="")
    else:
        print(f'{stack[i]}', end="")
print('>')