# Given a singly linked list, return the middle nofe of the list
# In case of even number of nodes, return the second middle node

#Defining the Node class
class Node():
    def __init__(self, data): 
        self.data = data      
        self.next = None      

#Defining the linked list class
class LinkedList():
    def __init__(self):
        self.head = None       
        self.tail = self.head  
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "\n")
            temp = temp.next


class Solution:
    def middleNode(self, head):
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        mid = count // 2
        temp = head
        for _ in range(mid):
            temp = temp.next
        return temp

if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:  # You can test with even number of elements too
        ll.append(val)

    ll.print_list()

    # Find and print the middle node
    sol = Solution()
    middle_node = sol.middleNode(ll.head)
    print(middle_node.data)
       