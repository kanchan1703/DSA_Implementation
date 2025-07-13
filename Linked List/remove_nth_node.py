# Remove the nth node from the end of a linked list.
# Given the head of a singly linked list and an integer n. Remove the nth node from the back of the linked List and return the head of the modified list. 

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
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> " if curr.next else "\n")
            curr = curr.next

    def removeNthFromEnd(self, n):
        fast = self.head
        slow = self.head

        for _ in range(n):
            if fast:
                fast = fast.next

        if not fast:
            self.head = self.head.next
            return

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next



if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.append(val)

    print("Original List:")
    ll.print_list()

    ll.removeNthFromEnd(2)  
    print("After Removing 2nd Node from End:")
    ll.print_list()
