#python program for tree trversal(DFS)

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key

# a function to do Inorder tree traversal

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data),
        printInorder(root.right)

# a function to do preorder tree traversal

def printpreorder(root):
    if root:
        print(root.data)
        printpreorder(root.left)
        printpreorder(root.right)

# A function to do postorder tree traversal

def printpostorder(root):
    if root:
        printpostorder(root.left)
        printpostorder(root.right)
        print(root.data)

# Driver code
Root=Node('Akilesh')
Root.left=Node('babureddy')
Root.right=Node('sai manish')
Root.left.left=Node('yashwanth')
Root.right.left=Node('kumar')
Root.right.right=Node('prashanth')
print("\n Inorder traversal of binary tree is")
printInorder(Root)
print("\n preorder traversal of binary tree is")
printpreorder(Root)
print("\n postorder traversal of binary tree is")
printpostorder(Root)
