"""
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""
from heapq import heappush, heappop

# 특정 정점 기준으로 시작
# - 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 간다
# --> 작은 노드를 먼저 꺼내기 위해 우선순위큐(heapq)를 활용한다.
def prim(start_node):
    pq = [(0, start_node)] # (가중치, 노드) 형태
    MST = [0] * V # visited 와 동일
    min_weight = 0 # 최소 비용
    
    while pq:
        weight, node = heappop(pq) # 가장 작은 가중치

        # 이미 방문한 노드라면 continue
        if MST[node]:
            continue
        
        MST[node] = 1 # node로 가는 최소 비용이 선택되었다
        min_weight += weight # 누적합 추가

        for next_node in range(V):
            # 갈 수 없으면 continue
            if graph[node][next_node] == 0:
                continue

            # 이미 방문했으면 continue
            if MST[next_node]:
                continue

            heappush(pq, (graph[node][next_node], next_node))
    
    return min_weight

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight # 양방향

result = prim() # 출발 정점과 함께 시작
print(f'최소 비용 = {result}')


# kruskal
def find_set(x):
    if x == parents[x]:
        return
    
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry: # 사이클 발생
        return
    
    # 일정한 규칙으로 병합
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry
    

V, E = map(int, input().split())

# 1. 간선들을 가중치 기준으로 정렬
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight)) # 간선들의 정보를 저장

# 가중치 기준 오름차순 정렬
edges.sort(key=lambda x: x[2])

# 2. 가중치가 작은 간선부터 순서대로 선택하자
# - 사이클이 발생하면 고르지 말자!
# - 언제까지 ?
# - MST 가 완성될 때까지
# - V-1 개를 선택할 때 까지
cnt = 0 # 현재까지 선택한 간선의 수
result = 0 # 가중치의 합

parents = [i for i in range(V)] # make_set


for u, v, w in edges:
    # 사이클이 아니라면
    # - 연결 (같은 집합으로 만든다)
    # - cnt += 1
    # - cnt가 V - 1 이라면 종료
    if find_set(u) != find_set(v): # u, v 사이클이 아니면
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1:
            break

print(f'최소 비용 = {result}')