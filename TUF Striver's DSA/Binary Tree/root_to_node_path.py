# Prob: Given a binary tree, return all the root-to-leaf path in any order

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None  # You had `def __init__(self, data)` — not required for general tree

    def insertNode(self, root, data):  # Need to use @staticmethod or make it an external function
        if root is None:
            return Node(data)
        elif root.data < data:
            root.right = Tree.insertNode(root.right, data)
        else:
            root.left = Tree.insertNode(root.left, data)
        return root
    
    # Function for root-to-left node path
    def leafPath(self, root):
        if not root:
            return []
        
        result = []
        stack = [(root, str(root.data))]
        
        while stack:
            node, path = stack.pop()

            #Condition for leaf node
            if not node.left and not node.right:
                result.append(path)

            # if right child node exist
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.data)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.data)))
            
        return result

t = Tree()
t.root = Node(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.right = Node(5)

# Call function
print(t.leafPath(t.root))