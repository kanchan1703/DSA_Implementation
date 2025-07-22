# Find Quads that add up to the target value

class Solution:
    # brute force appraoch
    # Time complexity: O(n^4)

    def fourSum(self, nums, target):
        n = len(nums)
        result = set()

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            quad = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                            result.add(quad)  

        return list(result)  
