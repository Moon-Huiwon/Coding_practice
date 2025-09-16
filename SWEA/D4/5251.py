# import sys
# sys.stdin = open('input.txt')

from heapq import heappop, heappush

def dijkstra(start_node):
    pq = [(0,start_node)]
    dists = [float('inf')] * (N+1) # 누적 거리 저장할 리스트
    dists[start_node] = 0 # 처음 노드는 누적 거리 0

    while pq:
        dist, node = heappop(pq) # 거리 / 노드

        if dists[node] < dist: # 더 작은 누적 거리가 저장되어있으면 continue
            continue

        for next_dist, next_node in graph[node]: # 연결된 노드의 거리 / 연결된 노드
            
            new_dist = dist + next_dist # 연결된 노드로 이동했을 때의 누적 거리
            
            if dists[next_node] <= new_dist: # 더 작은 누적 거리가 저장되어있으면 continue
                continue
            
            dists[next_node] = new_dist # 누적 거리 업데이트
            heappush(pq, (new_dist, next_node)) # pq에 저장
    
    return dists

T = int(input())
for t in range(T):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e)) # 단방향
    
    result = dijkstra(0)
    print(f'#{t+1} {result[-1]}')