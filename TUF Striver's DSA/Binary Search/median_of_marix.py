# Median of a matrix
class Solution:
    def findMedian(self, matrix):
        linear = []

        for i in matrix:
            for j in i:
                linear.append(j)

        linear.sort()

        n = len(linear)
        mid = n // 2

        if n % 2 == 1:
            return linear[mid]  
        else:
            return (linear[mid - 1] + linear[mid]) / 2.0


s = Solution()
print(s.findMedian([ [1, 4, 9], [2, 5, 6], [3, 7, 8] ]))