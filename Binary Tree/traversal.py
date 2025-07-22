# Binary Tree Traversal in a Binary Tree

class Node:
    def __init__(self, data=None):
        self.val = data
        self.left = None
        self.right = None

    def binary_tree(arr):
        if not arr:
            return None

        # Create Node instances
        nodes = [Node(val) for val in arr]

        for i in range(len(arr) // 2):
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < len(arr):
                nodes[i].left = nodes[left_index]
            if right_index < len(arr):
                nodes[i].right = nodes[right_index]

        return nodes[0]  # return root node


# Inorder Traversal (left->root->right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

# Pre-order Traversal (root->left->right)
def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

# Post order Traversal (left->right->root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')



# 

# Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = Node.binary_tree(arr)

    print("Inorder Traversal:    ", end="")
    inorder(root)
    print()

    print("Preorder Traversal:   ", end="")
    preorder(root)
    print()

    print("Postorder Traversal:  ", end="")
    postorder(root)
    print()

