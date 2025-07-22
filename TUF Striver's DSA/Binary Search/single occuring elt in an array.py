class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        left = 0
        right = n-1

        while left<right:
            mid = left + (right-left)//2

            if mid%2 ==1:
                mid = mid-1
            
            if nums[mid] == nums[mid+1]:
                left = mid+2
            else:
                right = mid
        
        return nums[left]

s = Solution()
print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8])) 