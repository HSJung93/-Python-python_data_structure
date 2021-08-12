from binary_tree import Node

def height(node):
    if node is None:
        return 0
    else:
        leftHeight = height(node.left)
        rightHeight = height(node.right)

        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1

def breadthFirstTraversal(root):
    if root == None:
        return 0
    else:
        h = height(root)
        for i in range(1, h + 1):
            printBFT(root, i)

def printBFT(root, level):
    if root is None:
        return
    else:
        if level == 1:
            print(root.data, end = ' ')
        elif level > 1:
            printBFT(root.left, level - 1)
            printBFT(root.right, level - 1)

if __name__ == '__main__':
    root = Node("Root")
    root.left = Node("L")
    root.right = Node("R")
    root.left.left = Node("LL")

    breadthFirstTraversal(root)