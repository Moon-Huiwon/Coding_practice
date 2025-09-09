T = int(input())
for t in range(T):
    N = int(input())
    corridor = [0]*200 # 복도 리스트 생성
    for _ in range(N):
        current, next = map(int, input().split()) # 현재 방 / 돌아갈 방
        current_idx = (current - 1) // 2 # 현재 방의 복도 idx 추출
        next_idx = (next - 1) // 2 # 돌아갈 방의 복도 idx 추출
        
        min_idx = min(current_idx, next_idx) # 최소값
        max_idx = max(current_idx, next_idx) # 최대값

        for i in range(min_idx, max_idx+1):
            corridor[i] += 1 # 해당 범위 안의 복도 idx에 +1 (복도를 지나갔음을 의미)
    
    print(f'#{t+1} {max(corridor)}') # 복도를 지나간 리스트에서 최대값 추출