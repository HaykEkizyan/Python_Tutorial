"""

Given a word, check whether it is a palindrome or not.
A string is considered to be a palindrome if it reads the same in both directions.

"""

def isWordPalindrome(word):   # Implement the missing code, denoted by ellipses.
    return word == word[::-1] # Reverse the string

print(isWordPalindrome("aba"))
print(isWordPalindrome("abab"))
print(isWordPalindrome("aibohphobia"))
print(isWordPalindrome("codedog"))
print(isWordPalindrome("b"))




