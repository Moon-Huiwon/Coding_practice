n = int(input())
nums = list(map(int, input().split()))
nums.sort()

i = 0
j = 2*n-1

W = []
while i < j:
    W.append(nums[i] + nums[j])
    i += 1
    j -= 1

print(min(W))