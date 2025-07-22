# 2 Sum Problem
#Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.

class Solution:
    # Brute force approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [] # in case no solution is found
    
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  
