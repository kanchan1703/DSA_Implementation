class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        return self.solve(n - 1, target, arr)

    def solve(self, i, target, arr):
        # in case target is 0
        if target == 0:
            return True

        # Array has 1 element
        if i == 0:
            return arr[0] == target

        # Excluding the current element
        not_pick = self.solve(i - 1, target, arr)

        # Including the current element 
        pick = False
        if arr[i] <= target:
            pick = self.solve(i - 1, target - arr[i], arr)

        return pick or not_pick
    
s = Solution()
# Example usage
arr = [3, 34, 4, 12, 5, 2]
target = 9
print(s.isSubsetSum(arr, target)) 