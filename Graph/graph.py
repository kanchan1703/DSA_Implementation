# Undirected Graph Implementation
# Graph is a data structure which contains nodes and edges, where nodes are connected to each other through edges.

# Some of the graph examples are trees and linked lists.
#Graphs can be reprsented in 3 ways:
# 1. Adjacency List: stores the nodes with which a particular node is connected to in a linked list or array.
#                   The lists or arrays are stored in hash tables with keys as nodes and value as adjacency list.
# 2. Adjacency Matrix: an nxn matrix, where n is no of nodes, M[i][j] = 1 if nodes i and j are connected otherwise 0.
# Edge List: ontains all the pairs of nodes which are connected, and if the graph is weighted, then the weight of each edge as well.

class Graph():
    # Constructor to initialize graph with empty adjacency list
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}
    
    # Function to insert node
    # value of the node as a key in the adjacency list and initialize the value of the key to be an empty array
    def inser_node(self, data):
        if data not in self.adjacency_list:
            self. adjacency_list[data] = []
            self.number_of_nodes += 1
        return
    
    # Insert edge method : two nodes between which the edge is to be inserted
    # First we will check if an edge already exists by checking the adjacency list of either of the two nodes.
    def insert_edge(self, vertex1, vertex2):
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return
        return "Edge already exists"
    
    # Print method
    def printGraph(self):
        for node in self.adjacency_list:
            print(f"{node} -> {', '.join(map(str, self.adjacency_list[node]))}")

    
graph = Graph()
# Inserting nodes
graph.inser_node(1)
graph.inser_node(2) 
graph.inser_node(3)
# Inserting edges
graph.insert_edge(1, 2)
graph.insert_edge(1, 3)
graph.insert_edge(2, 3)
# Printing the graph
graph.printGraph()

print(graph.adjacency_list)
print(graph.number_of_nodes)