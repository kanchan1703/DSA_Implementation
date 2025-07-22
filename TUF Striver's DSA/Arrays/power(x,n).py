# Power(x, n): returning the value of x raised to the power n

class Solution:
    def power(x, n):
        result = 1
        
        while n>0:
            if n % 2 == 1:
                result *= x
            x *= x
            n = n//2
        return result
    
s= Solution
print(s.power(2, 10))  
    

