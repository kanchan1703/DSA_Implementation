# Very very important, for interview point of view
# Queue implementation using stack

# 2 methods:
# 1. Using 2 stacks (enqueue is costly o(n))
# 2. Using 1 stack  (dequeue is costly o(n))


# Method 1
class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def peek(self):
        