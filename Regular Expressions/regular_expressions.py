"""

 Regular expressions are a powerful tool for various kinds of string manipulation.
 They are a domain specific language (DSL) that is present as a library in most
modern programming languages, not just Python.
 They are useful for two main tasks:
- verifying that strings match a pattern (for instance, that a string has the format of an email address),
- performing substitutions in a string (such as changing all American spellings to British ones).

 Domain specific languages are highly specialized mini programming languages.
 Regular expressions are a popular example, and SQL (for database manipulation) is another.
 Private domain-specific languages are often used for specific industrial purposes.


 Regular expressions in Python can be accessed using the re module, which is part of the standard library.
# import re
 After you've defined a regular expression, the re.match function can be used to determine whether it matches at the beginning of a string.
 If it does, match returns an object representing the match, if not, it returns None.
 To avoid any confusion while working with regular expressions, we would use raw strings as r"expression".
 Raw strings don't escape anything, which makes use of regular expressions easier.

"""

# 1

import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")        # Match

"""

 The above example checks if the pattern "spam" matches the string and prints "Match" if it does.
 Here the pattern is a simple word, but there are various characters, which would have special 
meaning when they are used in a regular expression.

"""

"""

 Other functions to match patterns are re.search and re.findall.
 The function re.search finds a match of a pattern anywhere in the string.
 The function re.findall returns a list of all substrings that match a pattern.
 
"""
