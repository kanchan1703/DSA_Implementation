class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def insertNode(self, root, data):
        if root is None:
            return Node(data)
        elif root.data < data:
            root.right = self.insertNode(root.right, data)
        else:
            root.left = self.insertNode(root.left, data)
        return root

    def morrisPreorder(self, root):
        current = root
        result = []

        while current:
            if current.left is None:
                result.append(current.data)
                current = current.right
            else:
                predecessor = current.left  # Rightmost node in left subtree
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    result.append(current.data)
                    predecessor.right = current  # Creating the thread
                    current = current.left
                else:
                    predecessor.right = None  # Removing the thread
                    current = current.right

        return result

# Create the tree
t = Tree(10)
t.root.left = Node(20)
t.root.right = Node(30)
t.root.left.left = Node(40)
t.root.left.right = Node(50)

# Print the tree root value (basic print)
print("Tree Root:", t.root.data)

# Perform Morris Preorder Traversal
output = t.morrisPreorder(t.root)
print("Morris Preorder Traversal:", output)
