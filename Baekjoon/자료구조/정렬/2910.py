N, C = map(int, input().split())

tmp_info = []

nums = list(map(int, input().split()))
for num in set(nums):
    cnt = nums.count(num)
    idx = nums.index(num)
    tmp_info.append((cnt, -idx, num))

tmp_info.sort(reverse=True)

ans = []
for cnt, _, num in tmp_info:
    ans.extend([num] * cnt)

print(*ans)