def traverse(node, tree):
    global cnt
    
    if node <= len(tree):
        # 왼쪽으로 이동
        traverse(node * 2, tree)
        # 값 업데이트
        cnt += 1
        # 해당 노드에 값 넣기
        cnt_num[node] = cnt
        # 오른쪽으로 이동
        traverse(node * 2 + 1, tree) 

T = int(input())
for t in range(T):
    # 노드 개수
    N = int(input())
    # 노드에 넣을 값
    cnt = 0
    cnt_num = [0] * (N+1)
    tree = [node for node in range(N)]

    traverse(1, tree)
    print(f'#{t+1} {cnt_num[1]} {cnt_num[N//2]}')
