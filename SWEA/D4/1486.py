# combinations 활용
from itertools import combinations

T = int(input())
for t in range(T):
    N, B = map(int, input().split()) # 점원 수 / 선반 높이
    H = list(map(int, input().split())) # 점원의 키

    height_diff = float('inf')
    for i in range(1, N+1): # 1~N개로 구성된 조합
        for comb in combinations(H, i): # 조합 찾기
            h_sum = sum(comb) # 조합 합
            if h_sum >= B: # 선반 높이 이상이면
                height_diff = min(height_diff, h_sum - B) # 높이의 차이 업데이트
            
    print(f'#{t+1} {height_diff}')

# 백트래킹 활용
def backtracking(index, value):
    global height_diff

    if value >= B:
        height_diff = min(height_diff, value - B)
        return

    for i in range(index, N):  # index부터 시작해서 중복 제거
        backtracking(i + 1, value + H[i])

T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    height_diff = float('inf')
    backtracking(0, 0)
    print(f'#{t+1} {height_diff}')