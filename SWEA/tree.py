# 배열로 표현한 이진 트리
tree = [node for node in range(17)]

# 2번 노드를 확인한다면
node = 2
# 2번 노드의 왼쪽 자식은 *2에 있다.
print(tree[node * 2])
# 2번 노드의 오른쪽 자식은 *2 + 1에 있다.
print(tree[node * 2 + 1])

# 10번 노드의 부모는
node = 10
print(tree[node // 2])

# 현재 노드와 전체 트리
def traverse(node, tree):
    # 현재 노드가 존재하는지를 파악
    if node < len(tree):
        # LVR
        # 먼저 왼쪽을 간다.
        traverse(node * 2, tree)
        # 그 다음 나를 방문한다.
        print(tree[node], end =' ')
        # 마지막으로 오른쪽을 간다.
        traverse(node * 2 + 1, tree)

# root는 1부터
traverse(1, tree)