# Diameter of a binary tree
# You have to find the longest path between any two nodes in the tree
# The path may or may not pass through the root

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if root is None:
            return Node(data)
        elif root.data < data:
            insert(root.right, data)
        elif root.data > data:
            insert(root.left, data)
        return data

    # Diameter Function
    def diameter(self):
        diameter_list = [0]  # Use a list to allow updates inside nested function

        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            # Update the diameter if the path through this node is larger
            diameter_list[0] = max(diameter_list[0], left_height + right_height)
            # Return height of this subtree
            return 1 + max(left_height, right_height)

        height(root)
        return diameter_list[0]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(Tree.diameter(root))  

