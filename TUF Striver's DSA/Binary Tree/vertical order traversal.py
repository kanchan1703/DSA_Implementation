# Vertical Order Traversal of Binary Tree
# The answer should be a list of top-to-bottom orderings for each column index starting from teh leftmost column

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insertNode(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insertNode(root.left, data)
        else:
            root.right = self.insertNode(root.right, data)
        return root

    


    def verticalTraversal(self, root):
        if not root:
            return []

        queue = deque([(root, 0)])  # node and horizontal distance
        column_map = {}

        while queue:
            node, hd = queue.popleft()

            if hd not in column_map:
                column_map[hd] = []
            column_map[hd].append(node.data)

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        result = []
        for col in range(min(column_map), max(column_map) + 1):
            result.append(column_map[col])
        return result

# example 
tree = Tree()
tree.root = tree.insertNode(tree.root, 10)
tree.insertNode(tree.root, 5)
tree.insertNode(tree.root, 15)
tree.insertNode(tree.root, 2)
tree.insertNode(tree.root, 20)

# Vertical Order Traversal
print(tree.verticalTraversal(tree.root))