# Level Order Traversal (Spiral form)

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
    
    def levelOrder(self, root):
        if not root:
            return 
        
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for i in range(level_size):
                node = queue.popleft()
                current_level.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            result.append(current_level)

        return result
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

# Call the function and print
output = levelOrder(root)
print(output)  
