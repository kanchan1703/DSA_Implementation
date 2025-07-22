# Right Side View of a Binary Tree

# We will be usign BFS apprach to solve the problem

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
            return(Node.data)
        elif root.data < data:
            root.right = Tree.insertNode(root.right, data)
        else:
            root.left = Tree.insertNode(root.left, data)
        return root
    
    # Right side view
    def right_side_view(self, root):
        if not root:
            return []
        
        result = [] #list to store the ans
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

            if i == level_size-1:
                result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

# Example Usage
t = Tree()
t.root = Node(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.right.right = Node(5)

print("Right Side View:", t.right_side_view(t.root))