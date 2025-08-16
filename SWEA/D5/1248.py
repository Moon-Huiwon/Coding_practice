# 조상 노드를 찾기 위한 함수
def par_dfs(S, adj, stack, visitied):
    
    stack.append(S)
    visitied[S] = 1
    
    for node in adj[S]:
        if visitied[node] == 0:
            par_dfs(node, adj, stack, visitied)
    
    return stack

# 서브 트리의 크기를 찾기 위한 함수
def count_dfs(S, adj, visitied):
    global cnt
    
    cnt += 1
    visitied[S] = 1
    
    for node in adj[S]:
        if visitied[node] == 0:
            count_dfs(node, adj, visitied)
    
    
T = int(input())
for t in range(T):
    V, E, node1, node2 = map(int, input().split())
    node_edge = list(map(int, input().split()))

    # 서브 트리의 크기를 알아내기 위한 adj
    sub_tree_adj = [[] for _ in range(10001)]
    # 부모 노드를 찾기 위한 adj
    par_adj = [[] for _ in range(10001)]
    for i in range(0, len(node_edge), 2):
        start_node = node_edge[i]
        end_node = node_edge[i+1]
        sub_tree_adj[start_node].append(end_node)
        par_adj[end_node].append(start_node)
    
    # 첫번째 정점의 조상 찾기 (조상 노드를 stack에 저장)
    par1_stack = []
    par1_visitied = [0] * 10001
    par_node1 = par_dfs(node1, par_adj, par1_stack, par1_visitied)
    
    # 두번째 정점의 조상 찾기 (조상 노드를 stack에 저장)
    par2_stack = []
    par2_visitied = [0] * 10001
    par_node2 = par_dfs(node2, par_adj, par2_stack, par2_visitied)
    
    # 가장 가까운 공통 조상 찾기
    par_node = 0
    for i in par_node1:
        if i in par_node2:
            par_node = i
            break
    
    # 공통 조상의 서브트리 찾기 (cnt로 서브 트리 크기 계산)
    sub_visitied = [0] * 10001
    cnt = 0
    count_dfs(par_node, sub_tree_adj, sub_visitied)

    print(f'#{t+1} {par_node} {cnt}')