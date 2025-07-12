# Nth root of an integer
# Given an integer n and a positive integer m, find the nth root of m.
class Solution:
    def NthRoot(self, n, m):
      low = 1
      high = m
      while low <= high:
        mid = (low + high) // 2
        power = mid ** n
        
        if power == m:
            return mid
        elif power < m:
            low = mid + 1
        else:
            high = mid - 1
            
      return -1  
    
s = Solution()
print(s.NthRoot(3, 27))  
print(s.NthRoot(2, 16))