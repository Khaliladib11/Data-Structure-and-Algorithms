# Tree Data Structure: consists of root node and childers

class Node:
    """
    Node class
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        


# There are three ways to visit a node in a tree

# In-Order Traversal: visit all nodes on the left, then the root, then all nodes to the right

def inOrder(root):
    if root:
        inOrder(root.left)
        print(str(root.value) + ' ->', end='')
        inOrder(root.right)


# Pre-Order Traversal: visit the root, then all nodes on the left, then all nodes to the right

def preOrder(root):
    if root:
        print(str(root.value) + ' ->', end='')
        preOrder(root.left)
        preOrder(root.right)
        
        

# Post-Order Travesal: visit all nodes on the left, then all nodes to the right, then the root

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(str(root.value) + ' ->', end='')



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal ")
    inOrder(root)

    print("\nPreorder traversal ")
    preOrder(root)

    print("\nPostorder traversal ")
    postOrder(root)