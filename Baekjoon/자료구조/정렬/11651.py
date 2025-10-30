N = int(input())

nums = []
for _ in range(N):
    x, y = map(int, input().split())
    nums.append((y, x))

nums.sort()

for y, x in nums:
    print(x, y)