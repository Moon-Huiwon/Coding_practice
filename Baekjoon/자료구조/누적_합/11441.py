# 시간초과
# import sys
# input = sys.stdin.readline

# N = int(input())
# nums = list(map(int, input().split()))
# M = int(input())
# for _ in range(M):
#     s, e = map(int, input().split())
#     print(sum(nums[s-1:e]))

#%%
import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")

N = int(input())
nums = list(map(int, input().split()))

for i in range(1,N):
    nums[i] += nums[i-1]

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    if s == 1:
        print(nums[e-1])
    else:
        print(nums[e-1] - nums[s-2])