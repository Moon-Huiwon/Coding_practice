import sys
sys.stdin = open('input.txt')

def dfs(start):
    global ans
    
    if start == G: # 도착 정점 번호에 도달하면
        ans += 1 # ans 업데이트
        return
    
    for node in nodes[start]: # 연결된 노드로 전부 탐색
        if visited[node] == 0: # 방문하지 않은 노드만 탐색
            visited[node] = 1 # 방문 처리
            dfs(node) # 함수 호출
            visited[node] = 0 # 백트래킹을 위해 방문 처리 초기화

T = int(input())
for t in range(T):
    N, E = map(int, input().split()) # 마지막 정점번호 / 간선 수
    nodes_list = list(map(int, input().split())) # info 받기
    S, G = map(int, input().split()) # 출발정점 / 도착정점
    nodes = [[] for _ in range(N+1)] # 각 노드에 연결된 노드들 받기
    for i in range(0,len(nodes_list),2):
        nodes[nodes_list[i]].append(nodes_list[i+1]) # 단방향
    visited = [0]*(N+1) # 방문 처리 리스트
    ans = 0
    dfs(S)
    print(f'#{t+1} {ans}')