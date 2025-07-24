# Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.

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
        elif root.data < data:
            root.right = Tree.insertNode(root.right, data)
        else:
            root.left = Tree.insertNode(root.left, data)
        return root
    
    # Max Depth Function (using BFS)
    def maxDepth(self, root):
        # Base case
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                depth += 1
        return depth

