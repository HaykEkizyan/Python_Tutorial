"""

There are various special sequences you can use in regular expressions.
They are written as a backslash followed by another character.
One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17.
This matches the expression of the group of that number.

"""

# 1

import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
   print ("Match 1")                            # Match 1

match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2")                            # Match 2

match = re.match(pattern, "abc cde")
if match:
   print ("Match 3")

# Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the first group's subexpression,
# which is the matched expression itself, and not the regex pattern.


"""

More useful special sequences are \d, \s, and \w.
These match digits, whitespace, and word characters respectively.
In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. 
For instance, \D matches anything that isn't a digit.

"""

# 2

import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")

if match:
   print("Match 1")                          # Match 1

match = re.match(pattern, "1, 23, 456!")
if match:
   print("Match 2")

match = re.match(pattern, " ! $?")
if match:
   print("Match 3")

# (\D+\d) matches one or more non-digits followed by a digit.

