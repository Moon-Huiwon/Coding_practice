import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")

N = int(input())

tree = {}

for _ in range(N):
    par, left, right = map(str, input().rstrip().split())
    
    tree[par] = (left, right)    

def preorder_traversal(node):
    if node == '.' or node not in tree:
        return

    print(node, end="")
    preorder_traversal(tree[node][0])
    preorder_traversal(tree[node][1])

def inorder_traversal(node):
    if node == '.' or node not in tree:
        return

    inorder_traversal(tree[node][0])
    print(node, end="")
    inorder_traversal(tree[node][1])

def postorder_traversal(node):
    if node == '.' or node not in tree:
        return

    postorder_traversal(tree[node][0])
    postorder_traversal(tree[node][1])
    print(node, end="")
        

preorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')