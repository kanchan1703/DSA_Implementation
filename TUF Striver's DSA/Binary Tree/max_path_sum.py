# Maximum Sum path in a binary tree
# A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

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
            return Node(data)
        elif root.data < data:
            root.right = self.insertNode(root.right, data)
        else:
            root.left = self.insertNode(root.left, data)
        return root
    
    def maxPathSum(self, root):
        
        sum = [float('-inf')]

        def dfs(node):
            nonlocal sum

            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            sum[0] = max(sum[0], node.data+left+right)

            return node.data + max(left, right)
        
        dfs(root)
        return sum[0]

t = Tree()
values = [-10, 9, 20, 15, 7]
for data in values:
    t.root = t.insertNode(t.root, data)

print("Maximum Path Sum:", t.maxPathSum(t.root))



