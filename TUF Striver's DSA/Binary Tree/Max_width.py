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
            root.right = self.insertNode(root.right, data)
        else:
            root.left = self.insertNode(root.left, data)
        return root
        
    # Max Width for the binary tree
    def maxWidth(self, root):
        # Base case
        if not root:
            return 0

        max_width = 0
        queue = deque() 
        queue.append((root, 0)) # stored as (node, index) pair in queue

        while queue:
            level_length = len(queue)
            first_node, first_index = queue[0]

            for i in range(level_length):
                node, index = queue.popleft()
                index -= first_index  # Normalize

                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

                if i == level_length - 1:
                    last_index = index

            max_width = max(max_width, last_index + 1)

        return max_width


t = Tree()
t.root = Node(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.right.right = Node(5)
print(t)


print(t.maxWidth(t.root))
