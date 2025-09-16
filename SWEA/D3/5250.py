# import sys
# sys.stdin = open('input.txt')

from heapq import heappop, heappush

def dijkstra(cx, cy):
    pq = [(0, cx, cy)]
    qtys = [[float('inf')] * N for _ in range(N)] # 각 정점까지의 최소 연료 소비량을 저장할 리스트
    qtys[cx][cy] = 0 # 시작 위치의 최소 연료 소비량은 0

    while pq:
        qty, cx, cy = heappop(pq) # 연료 소비량 / row / col

        if qtys[cx][cy] < qty: # continue
            continue

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]: # 상하좌우로 이동
            nx, ny = cx + dx, cy + dy
            
            if (nx < 0 or nx >= N) or (ny < 0 or ny >= N): # 인덱스 범위 외에 있으면 continue
                continue
            
            next_qty = qty + max(arr[nx][ny] - arr[cx][cy], 0) + 1 # 높이 차이만큼(더 높은 곳으로 이동할 경우) & 이동하면 +1

            if qtys[nx][ny] <= next_qty: # 업데이트 하지 않음
                continue

            qtys[nx][ny] = next_qty # 업데이트
            heappush(pq, (next_qty, nx, ny)) # pq에 넣기
    
    return qtys

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = dijkstra(0,0)
    print(f'#{t+1} {result[-1][-1]}')