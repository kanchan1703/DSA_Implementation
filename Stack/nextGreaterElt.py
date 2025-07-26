# Given a circular array, return the next greater element for every element in the array.
# The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner. 
# If it doesn't exist, return -1 for this element.

# Brute force approach
def nextGreaterElements(nums):
    n = len(nums)
    res = [-1] * n # intialising the result array with -1

    for i in range(n):
        for j in range(1, n):

            next_index = (i + j) % n # to handle the ciscular array

            if nums[next_index] > nums[i]:
                res[i] = nums[next_index]
                break                      # stop when we find the first greater elt
    return res


arr = [1,3,2,4]
print(nextGreaterElements(arr)) 