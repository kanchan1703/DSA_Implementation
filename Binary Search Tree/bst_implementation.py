# Binary Search Tree Implementation
# BST is a non-linear data structure, with o(log(n)) time complexity for search, insert, and delete operations on average.

# Worst case scenario: the bst becomes a linked list, leading to O(n) time complexity for these operations.

# Unbalanced BST
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BST class
class BST():
    def __init__(self):
        self.root = None
        self.no_of_nodes = 0

    # Insert method
    # Case 1: If the tree is empty, create a new node and set it as the root.
    # Case 2: If the tree is not empty, traverse the tree to find the correct position for the new node.
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            self.no_of_nodes += 1
            return
        else:
            current = self.root
            # Traverse the tree to find the correct position
            while(current.left != new_node) and (current.right != new_node):
                if new_node.data > current.data:
                    if current.right == None:
                        current.right = new_node
                    else:
                        current = current.right

                elif new_node.data < current.data:
                    if current.left == None:
                        current.left = new_node
                    else:
                        current = current.left

            self.no_of_nodes += 1
            return
        
    # Search method: Traverse the tree to find the node with the given data.
    def search(self, data):
        if self.root == None:
            return "tree is empty"
        else:
            current = self.root
            while current is not None:
                if data == current.data:
                    return "Node found"
                elif data < current.data:
                    current = current.left
                else:
                    current = current.right

    # Remove method: Remove a node with the given data from the tree.
    def remove(self, data):
        if self.root == None:
            return "Tree is empty"
        
        current = self.root
        parent_node = None

        # Traverse the tree to find the node to be removed
        while current is not None:
            if data < current.data:
                parent_node = current
                current = current.left
            elif data > current.data:
                parent_node = current
                current = current.right
            else: 
                # Node found
                #Node has left child only
                if current.right == None:
                    if parent_node == None:
                        self.root = current.left
                        return
                    else:
                        if parent_node.data > current.data:
                            parent_node.left = current.left
                            return
                        else:
                            parent_node.right = current.left
                            return
                #Node has right child only
                elif current.left == None:
                    if parent_node == None:
                        self.root = current.right
                        return
                    else:
                        if parent_node.data > current.data:
                            parent_node.left = current.right
                            return
                        else:
                            parent_node.right = current.right
                            return
                        
                #Node has both children
                elif current.left is not None and current.right is not None:
                    del_node = current.right
                    del_node_parent = current.right

                    # Loop to reach the leftmost node to the right child
                    while del_node.left is not None:
                        del_node_parent = del_node
                        del_node = del_node.left
                    current.data = del_node.data # the value of the replaced node is copied
                    
                    # If node to be deleted is the exact right child of the current node
                    if del_node == del_node_parent:
                        current.right = del_node.right
                        return 
                    # If the leftmost node of the right subtree of the current node has no right subtree
                    if del_node.right == None:
                        del_node_parent.left = None
                        return
                    # If the right subtree, we link it to the parent of the del_node
                    else:
                        del_node_parent.left = del_node.right
                        return
        return "Not found"            
    
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(13)
bst.insert(65)
bst.insert(0)
bst.insert(10)
