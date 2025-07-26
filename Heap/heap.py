# Heap: It is a tree where every parent is greater than its children (Max-heap) or smaller then its chilren (Min-heap)

# Max Heap/Min Heap are typically represented as arrays.
# arr[0]: root node
# arr[(i-1)/2]: parent node
# arr[(2*i)+1]: left child
# arr[(2*i)+2]: right child

# Operations in a Heap:
# 1. getMax(): to get teh max element  , T.C.= o(1)
# 2. extractMAx(): to remove the max elt, t.c= O(log n)
# 3. insert(): to insert a new element, t.c.= O(log n)

import sys
class maxHeap:
    # Constructor to initialize the heap
    # maxsize entered by the user, size set to 0, all the elements of heap set to 0
    def __init__(self, maxsize):
        self.maxsize = 0
        self.size =0
        self.Heap = [0] * (self.maxSize +1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1
