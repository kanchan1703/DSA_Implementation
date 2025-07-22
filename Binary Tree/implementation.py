class Node:
    def __init__(self, data=None):
        self.val = data
        self.left = None
        self.right = None

    def binary_tree(arr):
        if not arr:
            return None

        # Create list of nodes
        nodes = [Node(val) for val in arr]

        for i in range(len(arr) // 2):
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < len(arr):
                nodes[i].left = nodes[left_index]
            if right_index < len(arr):
                nodes[i].right = nodes[right_index]

        return nodes[0]
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    tree = Node.binary_tree(arr)
    print(tree.val)  # Output: 1