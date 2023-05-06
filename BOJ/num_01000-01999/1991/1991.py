import sys

N = int(sys.stdin.readline())
tree = {}

for n in range(N) :
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = [left, right]

def preorder(root) : # 전위순회
    if root != "." :
        print(root, end = "") # root
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right

def inorder(root) : # 중위순회
    if root != "." :
        inorder(tree[root][0])
        print(root, end = "")
        inorder(tree[root][1])


def postorder(root) : # 후위순회
    if root != "." :
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = "")

preorder("A")
print()
inorder("A")
print()
postorder("A")
