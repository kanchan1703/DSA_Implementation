# Array Implementation CRUD Operations
# In python arrays are already defined in the form of lists, herw we will be implementating using common methods

class Array:
    def __init__(self):
        self.length = 0  # Initialize the length of the array
        self.data = {}   # Use a dictionary to store elements with their indices
    
#The attributes of an array class are stored in dictionary by default
    #To print the array
    def __str__(self):
        print(self.data.values())
        return str(self.__dict__)
    
    #To get the values of the array, using index as the key
    def get(self, index):
        return self.data[index] 
    
    #Adding elements to the array
    def push(self, item):
        self.length += 1
        self.data[self.length-1] = item # Add the item at the end of the array
    
    #Inserting an element at a specific index
    def insert(self, index, item):
        self.length += 1
        for i in range(self.length-1, index, -1):
            self.data[i] = self.data[i-1]        #shifting the elements to the end by one place towards right
        self.data[index] = item

    #Deleting the last element of the array in o(1) time complexity
    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    
    #Deleting an element at a specific index
    def delete(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1] 
        self.length -= 1

arr = Array()
arr.push(6)
arr.push(2)
arr.push(9)
arr.push(45)
arr.push(12)
arr.push(67)

arr.pop()

arr.insert(3,10)
arr.delete(4)

print(arr)
    