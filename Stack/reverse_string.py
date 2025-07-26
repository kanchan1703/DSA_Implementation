# reverse words in the string

class Solution:
    def reverseWords(self, s):
        words = s.split()
        stack = []

        for word in words:
            stack.append(word)
        
        result = []

        while stack:
            top_word = stack.pop()
            result.append(top_word)

        return " ".join(result)
    

s = Solution()
print(s.reverseWords("the sky is blue"))  