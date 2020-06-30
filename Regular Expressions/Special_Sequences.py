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

"""

Additional special sequences are \A, \Z, and \b.
The sequences \A and \Z match the beginning and end of a string, respectively.
The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. 
Informally, it represents the boundary between words.
The sequence \B matches the empty string anywhere else.

"""

# 3

import re

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
   print("Match 1")                                # Match 1

match = re.search(pattern, "We s>cat<tered?")
if match:
   print("Match 2")                                # Match 2

match = re.search(pattern, "We scattered.")
if match:
   print("Match 3")

# "\b(cat)\b" basically matches the word "cat" surrounded by word boundaries.



"""

Email Extraction

To demonstrate a sample usage of regular expressions, lets create a program to extract email addresses from a string.
Suppose we have a text that contains an email address:

   str = "Please contact info@sololearn.com for assistance"
   
Our goal is to extract the substring "info@sololearn.com".
A basic email address consists of a word and may include dots or dashes.
This is followed by the @ sign and the domain name (the name, a dot, and the domain name suffix).
This is the basis for building our regular expression.

   pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
   
[\w\.-]+ matches one or more word character, dot or dash.
The regex above says that the string should contain a word (with dots and dashes allowed), followed by the @ sign, 
then another similar word, then a dot and another word.

Our regex contains three groups:
1 - first part of the email address.
2 - domain name without the suffix.
3 - the domain suffix.

"""

