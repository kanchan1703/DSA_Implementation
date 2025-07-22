# Depth First Search
# It is a types of vertical exploration, where you go deep down as possible before backtracking.
# we use STACK data structure 

# Types of DFS traversals: inorder, Preorder, Postorder
# Time compalxity: o(n), Space complexity: o(1)

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

    def dfs(self, root):
        if not root:
            return
        
        stack = [root]

        while stack:
            node = stack.pop()
            print(node.data, end =" ")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

t = Tree()
t.root = Node(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.left.right = Node(5)
t.root.right.right = Node(6)

t.dfs(t.root)


