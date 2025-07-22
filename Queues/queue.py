# Queue implementation using Lined List and CRUD operations

#Queue follows FIFO rule (First In First Out), like a reaf-life queue.
#Queue can be implemented using Arrays and Linked Lists.
# Queue using Arrays: the implementation is inefficient, as while removing an elt from teh front of the queue(array), we have to update teh queue everytme  making it an o(n) operation.
# Queue using Linked Lists: the implementation is efficient, as we can add and remove elts from both ends of the queue in o(1) time complexity.

#Time Complexity of Queue operations: 
#Peek - o(1) time complexity
#Enqueue - o(1) time complexity
#Dequeue - o(1) time complexity

#Node class: initializing the node with data and next pointer, contructor initializing the queue
class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

#Queue class: 
# 'first' pointer: points to the first node of the queue
# 'last' pointer : points to the last node of the queue

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    # Peek method: return the first elt of the queue
    def peek(self):
        return self.first.data

    # Enqueue method: add an elt to the end of the queue , time complexity is o(1)
    def enqueue(self, data):
        new_node = Node(data)
        #Case 1: Empty queue
        if self.last == None:
            self.first = self.last
            self.length += 1
            return
        #case 3: Non-empty queue
        else:
            self.last.next = new_node # pointing the last node to teh new node
            self.last = new_node      # updating the last node
            self.length += 1
            return
        
    # dequeue method: removing the first elt of the queue, time complexity is O(1)
    def dequeue(self):
        # Case 1: Empty queue
        if self.last == None:
            return None
        #case 2: Non-empty queue
        else:
            if self.last == self.first:  # queue has only one elt
                self.last = None
            else:                        # queue has more than one elt
                self.first = self.first.next
                self.length -= 1
            return 

    # Print Method for the queue
    def printQueue(self):
        if self.length == 0:
            print("Queue is empty")
            return
        else:
            current_pointer = self.first
            while (current_pointer != None):
                if current_pointer.next == None:
                    print(current_pointer.data)
                else:
                    print(current_pointer.data, end = " -> ")
                current_pointer = current_pointer.next
        return

    

queue = Queue()
queue.enqueue("this")
queue.enqueue("is")
queue.enqueue("a")
queue.enqueue("queue")

queue.printQueue()

queue.dequeue()
queue.dequeue()

queue.printQueue()
           

    