# Stacks are linear data structures and can be implemented using linked lists
# Stack follows LIFO rule (i.e. Last In First Out), hence insertion and deletion can take place from only one side

#The main opeations of a stack are:
#Push -o(1) time complexity
#Pop - o(1) time complexity
#Peek - o(1) time complexity

# Node class
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
#Stack class
class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    #Peek method: returns the elt at teh top of the Stack without removing it from teh stack
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    #Push method: adds an elt to the top of the stack
    def push(self, data):
        new_node = Node(data)
        if self.top == None:      # stack is empty
            self.top = new_node
            self.bottom = new_node
            self.length = 1
        else:                     #we make the next of the new node, which was pointing to None, point to the present top and then update the top pointer
            new_node.next = self.top
            self.top = new_node
            self.length += 1

    #Pop method: removes top elt from the stack
    def pop(self):
        if self.top is None:     # stack is empty
            print("Empty Stack")
        else:                    # we remove the top node by making the top pointer point to the next node
            self.top = self.top.next
            self.length -= 1
            if(self.length == 0): # we make the bottom pointer None if the stack becomes empty after popping
                self.bottom = None

    # Print method 
    def print_stack(self):
        if self.top is None:
            print("Empty Stack")
        else:
            current_pointer = self.top
            while(current_pointer!=None):
                print(current_pointer.data)
                current_pointer = current_pointer.next

my_stack = Stack()
print(my_stack.peek())

my_stack.push("google")
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_stack()

print(my_stack.top.data)
print(my_stack.bottom.data)

my_stack.pop()
my_stack.print_stack()