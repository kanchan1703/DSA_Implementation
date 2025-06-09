# Given an array of size n, return the majority elt of the array(appearing more than n/2 times)

class Solution:
#brute frorce appraoch
#Time Compelxity : o(n^2)
#Space complexity: o(1)
    def majorityElement(nums):
        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1
            if count > n // 2:
                return nums[i]
        return -1

# Approach 2: HAshmap


s = Solution()
print(s.majorityElement([3, 2, 3]))  
