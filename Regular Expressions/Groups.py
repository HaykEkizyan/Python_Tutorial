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
    print(match.group())                        # abcdefghi
    print(match.group(0))                       # abcdefghi
    print(match.group(1))                       # bc
    print(match.group(2))                       # de
    print(match.groups())                       # ('bc', 'de', 'fgh', 'g')

# Groups can be nested.

# 2.1

x = r"1(23)(4(56)78)9(0)"
y = re.match(x, "1234567890")
print(y.group(3))                               # 56

"""

There are several kinds of special groups.
Two useful ones are named groups and non-capturing groups.
Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. 
They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
Non-capturing groups have the format (?:...). 
They are not accessible by the group method, so they can be added to an existing regular expression 
without breaking the numbering.

"""

# 3

import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))                     # abc
    print(match.groups())                           # ('abc', 'ghi')

"""

Another important metacharacter is |.
This means "or", so red|blue matches either "red" or "blue".

"""

import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print("Match 1")                    # Match 1

match = re.match(pattern, "grey")
if match:
    print("Match 2")                    # Match 2

match = re.match(pattern, "griy")
if match:
    print("Match 3")

