nums = []

tmp_list = list(map(str, input().split()))
n = int(tmp_list.pop(0))

for num in tmp_list:
    nums.append(int(num[::-1]))

while len(nums) < n:
    tmp_nums = list(map(str, input().split()))
    for num in tmp_nums:
        nums.append(int(num[::-1]))

nums.sort()

for num in nums:
    print(num)