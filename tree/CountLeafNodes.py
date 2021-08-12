from binary_tree import Node

def countLeafNodes(root):
    if root is None:
        return 0
    if(root.left is None and root.right is None):
        return 1
    else:
        return countLeafNodes(root.left) + countLeafNodes(root.right)

if __name__ == '__main__':
    root = Node("Root")
    root.setLeft(Node("L"))
    root.setRight(Node("R"))
    root.left.setLeft(Node("LL"))

    print('Count of leaf nodes:',countLeafNodes(root))