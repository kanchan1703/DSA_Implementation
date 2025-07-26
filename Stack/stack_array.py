# Stack Implemntation using Arrays, CRUD operations
class Stack:
    #Constructor
    def __init__(self):
        self.array = []

    #Push Operation
    def push(self, data):
        self.array.append(data)
        return 
    
    # Pop Operation
    def pop(self):
        if len(self.array) != 0:
            self.array.pop()     # In-built pop function, to remove the element
            return
        else:
            print("Empty Stack")
            return
        
    # Peek Operation: to access the top element of the stack(last elt of the array)
    def peek(self):
        return self.array[len(self.array)-1]
    
    #Printing the Stack: traversing the entire array, space complexity O(n)
    def print(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i])
        return

    
#Calling the Stack class
my_stack = Stack()
my_stack.push("Python")
my_stack.push("is a")
my_stack.push("dynamically")
my_stack.push("typed")
my_stack.push("language.")
my_stack.print()

my_stack.pop()
my_stack.pop()
my_stack.print()

print(my_stack.peek())  
print(my_stack.__dict__)


