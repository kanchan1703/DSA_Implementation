# Kth elt in two sorted arrays
class Solution:
    def kthElement(self, a, b, k):
        m, n = len(a), len(b)
        i = j = 0
        merged = []
        
        while i < m and j < n:
            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
            
            if len(merged) == k:
                return merged[-1]
            
        # Leftover elts in array a
        while i < m and len(merged) < k:
            merged.append(a[i])
            i += 1
        
        # Leftover elts in array b
        while j < n and len(merged) < k:
            merged.append(b[j])
            j += 1

        return merged[-1]  

s=Solution()
# Example usage
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
print(s.kthElement(a, b, k))  
