# Zigzag Level Order Traversal in a binary tree

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def zigzag_traversal(self):
        if self.root is None:
            return []

        queue = deque([self.root])
        left_to_right = True
        result = []

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if left_to_right:
                result.extend(level_nodes)
            else:
                result.extend(reversed(level_nodes))

            left_to_right = not left_to_right

        return result

# Example usage
t = Tree()
t.root = t.insert(t.root, 1)
t.root = t.insert(t.root, 2)
t.root = t.insert(t.root, 3)
t.root = t.insert(t.root, 4)

print(t.zigzag_traversal())

    

