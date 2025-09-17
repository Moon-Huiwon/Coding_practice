# import sys
# sys.stdin = open('input.txt')

from heapq import heappop, heappush

def dijkstra(cx, cy):

    pq = [(0, cx, cy)]
    times = [[float('inf')] * N for _ in range(N)]
    times[cx][cy] = 0

    while pq:
        time, cx, cy = heappop(pq)

        if times[cx][cy] < time:
            continue

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = cx + dx, cy + dy

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            next_time = time + int(arr[nx][ny])

            if times[nx][ny] <= next_time:
                continue

            times[nx][ny] = next_time
            heappush(pq, (next_time, nx, ny))
    
    return times[-1][-1]


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = dijkstra(0,0)
    print(f'#{t+1} {ans}')
