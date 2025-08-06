## sort 함수 없이 코드 구성
T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    num_cnt = [0] * (max(nums)+1)
    for num in nums:
        num_cnt[num] += 1

    sort_num = []
    for i in range(len(num_cnt)):
        if num_cnt[i] > 0:
            sort_num.extend([i]*num_cnt[i])
            num_cnt[i] = 0

    print(f'#{t + 1}', end=" ")
    print(*sort_num)

## sort 함수를 사용하여 코드 구성
# T = int(input())
# for t in range(T):
#     N = int(input())
#     num_list = list(map(int, input().split()))
#     num_list.sort()
#
#     print(f'#{t+1}', end=" ")
#     print(*num_list)
