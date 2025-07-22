# Level Order Traversal of a Binary Tree
# In this traversal, we visit all nodes at the present depth level before moving on to nodes at the next depth level.
# Implemented using a queue (FIFO) data structure.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
	def __init__(self, data):
		self.root = Node(data)
		
	def insertNode(root, data):
		if(root==None):
			root=Node(data)
		elif(root.data < data):
			root.right=Tree.insertNode(root.right, data)
		else:
			root.left=Tree.insertNode(root.left, data)
		return root
    
	# Depth First Search
	



	

        
			
   

