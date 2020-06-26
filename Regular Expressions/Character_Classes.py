"""

Character classes provide a way to match only one of a specific set of characters.
A character class is created by putting the characters it matches inside square brackets.

"""

# 1

import re

pattern = r"[aeiou]"

if re.search(pattern, "gray"):
    print("Match 1")                    # Match 1 -> a matchs

if re.search(pattern, "qwertyuiop"):
    print("Match 2")                    # Match 2 -> e, i, o and u are match

if re.search(pattern, "rhythm myths"):
    print("Match 3")

# The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.

