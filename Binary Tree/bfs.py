from collections import deque

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None  

    def insertNode(self, root, data):  
        if root is None:
            return Node(data)
        elif root.val < data:
            root.right = Tree.insertNode(root.right, data)
        else:
            root.left = Tree.insertNode(root.left, data)
        return root

    def bfs(self, root):  # Use staticmethod if calling from outside without 'self'
        if not root:
            return
        
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            print(node.data, end=' ') 
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Driver Code
t = Tree()
t.root = Node(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.right = Node(4)
t.root.left.left = Node(5)
t.root.right.left = Node(6)
t.root.right.right = Node(7)

t.bfs(t.root)  # Call bfs with the root node
