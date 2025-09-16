# import sys
# sys.stdin = open('input.txt')

from heapq import heappop, heappush

def prim(start_node):
    pq = [(0, start_node)]
    MST = [0] * (V+1) # visited 와 동일한 역할
    min_weight = 0 # 최종 가중치

    while pq:
        weight, node = heappop(pq) # 가중치 / 노드

        if MST[node]: # 방문한 노드면 continue
            continue

        MST[node] = 1 # 방문 처리
        min_weight += weight # 최종 가중치에 현재 가중치 더해주기

        for next_node in graph[node]: # 연결된 노드들로 이동
            if MST[next_node[0]]: # 방문한 노드면 continue
                continue

            heappush(pq, (next_node[1], next_node[0])) # pq에 넣어놓기
    
    return min_weight

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((n2, w))
        graph[n2].append((n1,w))
    
    result = prim(0)
    print(f'#{t+1} {result}')