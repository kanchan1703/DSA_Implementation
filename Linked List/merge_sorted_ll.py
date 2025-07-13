# Merge two sorted linked lists within the LinkedList class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    # This method does not rely on self, so it can be a @staticmethod
    @staticmethod
    def mergeLinkedlist(l1, l2):
        dummy = Node(-1)
        current = dummy

        while l1 and l2:
            if l1.data < l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next

# Main block
if __name__ == "__main__":
    
    l1 = LinkedList()
    for val in [1, 3, 5]:
        l1.append(val)

    
    l2 = LinkedList()
    for val in [2, 4, 6]:
        l2.append(val)

    print("List 1:")
    l1.print_list()
    print("List 2:")
    l2.print_list()

    
    merged_head = LinkedList.mergeLinkedlist(l1.head, l2.head)

   
    print("Merged Sorted List:")
    temp = merged_head
    while temp:
        print(temp.data, end=" -> " if temp.next else "\n")
        temp = temp.next
