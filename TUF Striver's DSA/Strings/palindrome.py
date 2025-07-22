# Longest Palindrome Subset
#Given a string s, return the longest palindromic substring in s.
#A palindromic substring is a contiguous sequence of characters within the string that reads the same forward and backward.
# ATTENTION IS ALL I NEED
class Solution:
    def longestPalindrome(self, s):
        result = ""
        # Case1: Odd length palindrome
        for i in range(len(s)):
            left, right = i, i # ANINA 
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(result): 
                    result = s[left:right+1] 
                    # Print the result every time
                    print(result) 
                left -= 1
                right += 1

        # Case 2: Even length palindrome
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(result):
                    result = s[left:right+1]
                    print(result)
                left -= 1
                right += 1

        return result

s = Solution()
print(s.longestPalindrome("babad")) 

print("-----")
print(s.longestPalindrome("anine"))   
