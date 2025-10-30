N = int(input())

nums = []
for _ in range(N):
    x, y = map(int, input().split())
    nums.append((x, y))

nums.sort()

for x, y in nums:
    print(x, y)
