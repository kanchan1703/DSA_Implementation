# LPS (Longest Palindromic Substring) algorithm implementation

# We have to find the longest palindromic substring in a given string.
# We will be using the expand around center technique and then recursion.

def longest_palindromic_substring(s:str) -> str:
    # Creating a function to expand around the center of a potential palindrome
    def expand_around_center(left:int, right:int) -> str:
        
        # while loop(as we do not know the length of the palindrome)
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    # Loop through each character in the string
    for i in range(len(s)):
        # Case 1: Odd length palindromes
        odd = expand_around_center(i, i)
        # Case 2: Even length palindromes
        even = expand_around_center(i, i + 1)

        # Update longest if we found a longer palindrome
        if len(odd) > len(longest):  
            longest = odd               
        if len(even) > len(longest):
            longest = even
    return longest


# Example usage
if __name__ == "__main__":
    input_string = "babad"
    result = longest_palindromic_substring(input_string)
    print(f"The longest palindromic substring in '{input_string}' is: '{result}'")
