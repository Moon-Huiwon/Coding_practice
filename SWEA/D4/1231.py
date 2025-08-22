# 현재 노드와 전체 트리
def traverse(node, tree):
    # 현재 노드가 존재하는지를 파악
    if node < len(tree):
        # LVR
        # 먼저 왼쪽을 간다.
        traverse(node * 2, tree)
        # 그 다음 나를 방문한다.
        print(tree[node], end ='')
        # 마지막으로 오른쪽을 간다.
        traverse(node * 2 + 1, tree)


for t in range(10):
    N = int(input())
    # 각 노드에 해당하는 word 저장하는 공간
    words = [0] * (N+1)
    for _ in range(N):
        data = list(map(str, input().split()))
        # 노드 번호
        num = int(data[0])
        # 노드에 들어갈 word
        word = data[1]
        # 각 노드에 해당하는 word 저장
        words[num] = word
    
    print(f'#{t+1}', end=" ")
    traverse(1, words)
    print()