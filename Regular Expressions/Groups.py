"""

A group can be created by surrounding part of a regular expression with parentheses.
This means that a group can be given as an argument to metacharacters such as * and ?.

"""

# 1

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")                        # Match 1

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")                        # Match 2

if re.match(pattern, "spam"):
    print("Match 3")

# (spam) represents a group in the example pattern shown above.

"""

The content of groups in a match can be accessed using the group function.
A call of group(0) or group() returns the whole match.
A call of group(n), where n is greater than 0, returns the nth group from the left.
The method groups() returns all groups up from 1.

"""

# 2

import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

# Groups can be nested.

