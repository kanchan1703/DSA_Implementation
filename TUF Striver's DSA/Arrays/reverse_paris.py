# Reverse Pairs
# Given an array, return the number of reverse pairs on the array

#An index pair (i, j) is called a reverse pair if:
#0 <= i < j < nums.length
#nums[i] > 2 * nums[j].

class Soultion: 
    
    # Brute force approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def reversePairs(self, nums):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > 2 * nums[j]:
                    count += 1
        return count
    

s = Soultion()
print(s.reversePairs([1, 3, 2, 3, 1]))  