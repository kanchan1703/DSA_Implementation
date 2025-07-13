#Linked List CRUD Operations
#Linked List is a data structure, which consists of nodes and each node consists of data and pointer to the next node.

#Defining the Node class
class Node():
    def __init__(self, data): #passing data to the node
        self.data = data      # data is being stored in the node
        self.next = None      # the next pointer is initialized to None

#Defining the linked list class
class LinkedList():
    def __init__(self):
        self.head = None       # the head of the linked list is initialized to None
        self.tail = self.head  #since the lsit is empty, the tail point to the head
        self.length = 0        # the length of the linked list is initialized to 0

#Inserting the node at the end of the linked list
    def append(self, data):
        new_node = Node(data)   #creating a new node with the data passed
        #Case 1: Linked list is empty
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        #Case 2: Linked list is not empty
        else:
            self.tail.next = new_node  #the current tail next pointer sets to teh new node
            self.tail = new_node       # the tail pointer is updated to the new node
            self.length += 1           # increase the leanth by one node

# Inserting the node at the beginning of the linked list
    def prepend(self, data):
        new_node = Node(data)
        #Case 1: Linked list is empty
        if self.head == None:
            self.head = new_node   # moving the head pointer to the new node
            self.tail = self.head  # updating the tail pointer to the head node since hte lsit is empty
            self.length = 1        #updating hte length by 1
        #Case 2: Linked list is not empty
        else:
            new_node_next = self.head # the new node's next pointer will point to the current head
            self.head = new_node      # the head pointer is updated to the new node
            self.length += 1          # increasing the legnth by a node

# Inserting the node at a specific position in the linked list
    def insert(self, position, data):
        if position >= self.length:     # if the position is greater than or equal to the length of the list
            if position>self.length:    # we apply the append fucntion for inserting the node
                print("This position is not available. Inserting at the end of the list")
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        elif position == 0:            # the position is 0, we apply the prepend function
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:                          # the position to insert is a position "i" of the linked list
            new_node = Node(data)
            current_node = self.head
            for i in range(position-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

#Deleting a node from the linked list 
    #Delete by Value Method
    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next==None:
                self.tail = self.head
            self.length -= 1
            return
        while current_node.next!= None and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next!=None:
            current_node.next = current_node.next.next
            if current_node.next == None:
                self.tail = current_node
            self.length -= 1
            return
        else:
            print("Given value not found.")
    
    #Delete by Position Method
    def delete_by_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        if position>=self.length:
            position = self.length-1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return

# Printing the linked list
    def print_list(self):
        if self.head == None:
            print("Empty List")
        else:
            curr_node = self.head               # starting from the head
            while curr_node != None:            # traversing the linked list until the end
                print(curr_node.data, end=' ')  # printing the data of the current node
                curr_node = curr_node.next      # moving to the next node
            print()



# Calling out the functions to test the linked list
if __name__ == "__main__":
    ll = LinkedList()  # creating a new linked list object
    ll.append(10)      # appending 10 to the linked list
    ll.append(20)      # appending 20 to the linked list
    ll.prepend(5)      # prepending 5 to the linked list
    ll.print_list()    # printing the linked list
    print("Length of the linked list:", ll.length)  # printing the length of the linked list