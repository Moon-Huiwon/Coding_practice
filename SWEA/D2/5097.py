T = int(input())
for t in range(T):
    # N: 숫자 개수 M: 작업 횟수
    N, M = map(int, input().split())
    # 숫자 수열
    nums = list(map(int, input().split()))

    # index 순서
    # ex) nums = [5527, 731, 31274] 일 때
    # M = 1 : nums[1] / M = 2 : nums[2] / M = 3 : nums[0]
    # 따라서 idx_sequence = [1, 2, 0] 으로 반복된다.
    idx_sequence = [i for i in range(1, N)] + [0]
    
    # 따라서 수열의 맨 앞에 있는 숫자의 index = M % N 와 동일
    ans_idx = M % N

    print(f'#{t+1} {nums[ans_idx]}')