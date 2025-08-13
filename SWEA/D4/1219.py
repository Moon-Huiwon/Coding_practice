# import sys
# sys.stdin = open('input.txt')

def dfs(S):
    # 도착 노드(99)를 방문했다면 중단
    if 99 in stack:
        return
    
    # 방문 노드 stack에 넣기
    stack.append(S)
    # 방문 여부 표시하기
    visitied[S] = 1

    # 현재 노드와 엣지로 연결되어있는 노드들 방문하지 않았다면 방문하기
    for node in adj[S]:
        if visitied[node] == 0:
            dfs(node)


for _ in range(10):
    # 케이스 번호와 길이 받기
    case_num, length = map(int, input().split())
    # 노드는 0~99로 구성되어있으므로 0~99의 index를 노드 번호로 사용
    adj = [[] for _ in range(100)]
    # 2개씩 노드가 서로 연결되어있음을 보여주는 pair_list 받기
    pair_list = list(map(int, input().split()))
    # 노드가 2개씩 짝이므로 range의 step=2로 설정
    # 첫번째는 현재(시작하는) 노드, 두번째는 연결된 노드
    for i in range(0, len(pair_list), 2):
        start = pair_list[i]
        end = pair_list[i+1]
        adj[start].append(end) # 단방향
    
    # 방문 여부 처리하는 리스트
    visitied = [0] * 100
    
    # 방문하면 stack에 쌓기
    stack = []
    # 시작노드(0)부터 탐색 시작
    dfs(0)
    
    # 도착노드(99)를 방문했다면 stack에 99가 들어가있음
    if 99 in stack:
        print(f'#{case_num} 1')
    else:
        print(f'#{case_num} 0')
    
        