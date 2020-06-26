"""

Character classes provide a way to match only one of a specific set of characters.
A character class is created by putting the characters it matches inside square brackets.

"""

# 1
"""
import re

pattern = r"[aeiou]"

if re.search(pattern, "gray"):
    print("Match 1")                    # Match 1 -> a matchs

if re.search(pattern, "qwertyuiop"):
    print("Match 2")                    # Match 2 -> e, i, o and u are match

if re.search(pattern, "rhythm myths"):
    print("Match 3")
"""
# The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.

"""

Character classes can also match ranges of characters.
Some examples:
The class [a-z] matches any lowercase alphabetic character.
The class [G-P] matches any uppercase character from G to P.
The class [0-9] matches any digit.
Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.

"""

# 2

import re

pattern = r"[0-9][a-z][a-z]"

if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("match 2")

if re.search(pattern, "1ab"):
    print("Match 3")                # Match 3

#2.1

import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
   print("Match 1")                 # Match 1

if re.search(pattern, "E3"):
   print("Match 2")

if re.search(pattern, "1ab"):
   print("Match 3")

# The pattern in the example above matches strings that contain two alphabetic uppercase letters followed by a digit.