def find_cnt(N, A, B, cnt):
    if N < 2:
        return -1
    
    if N % 2 == 1:
        N += 1

    nums = [0 for _ in range(N+1)]
    nums[A] = 'KIM'
    nums[B] = 'IM'
    for i in range(1, N+1, 2):
        if nums[i] != 0 and nums[i+1] != 0:
            return cnt
    
    return find_cnt(N//2, (A+1)//2, (B+1)//2, cnt+1)
    

N, A, B = map(int, input().split())
cnt = find_cnt(N,A,B,1)
print(cnt)