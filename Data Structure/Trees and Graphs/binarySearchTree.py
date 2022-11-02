# Binary Search Tree:
# all nodes on the left subtree are less than the root node
# all node on the right subtree are greater than the root node

# Worset Case scenario:
# - Search: O(n)
# - Insert: O(n)
# - Delete: O(n)


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    

def inOrder(node):
    if node:
        inOrder(node.left)  # Traverse left
        print(str(node.value) + ' ->', end='')  # Traverse root
        inOrder(node.right)  # Traverse Right


# Insert a node
def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.value:
        node.left = insert(node.left, key)
    
    else:
        node.right = insert(node.right, key)

    return node

# Find the inorder successor 
def minValueNode(node):
    current = node

    while current:
        current = current.left

    return current


# Delete a node
def deleteNode(node, key):
    
    # if the tree is empty
    if node is None:
        return node

    
    # find the node to be deleted
    if key < node.value:
        node.left = deleteNode(node.left, key)
    elif key > node.value:
        node.right = deleteNode(node.right, key)

    else:
        if node.left is None:
            tmp = node.right
            node = None
            return tmp

        elif node.right is None:
            tmp = node.left
            node = None
            return tmp
        
        tmp = minValueNode(node.right)
        node.value = tmp.value
        node.right = deleteNode(node.right, tmp.value)

    return node
    

if __name__ == '__main__':
    root = None
    root = insert(root, 8)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 14)
    root = insert(root, 4)

    print("Inorder traversal: ", end=' ')
    inOrder(root)

    print("\nDelete 10")
    root = deleteNode(root, 10)
    print("Inorder traversal: ", end=' ')
    inOrder(root)