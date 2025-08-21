import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())
nums = [i+1 for i in range(N)]
remove_cnt = 0

# 처음 제거될 사람
idx = K - 1
while len(nums) > 1:
    idx %= len(nums)
    print(nums.pop(idx))
    remove_cnt += 1
    # 왼쪽
    if (remove_cnt // M) % 2 == 1:        
        idx = (idx - K) + len(nums)
    # 오른쪽
    else:    
        idx += K -1

print(nums.pop(0))
