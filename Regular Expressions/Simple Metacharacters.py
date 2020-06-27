"""

Metacharacters are what make regular expressions more powerful than normal string methods.
They allow you to create regular expressions to represent concepts like "one or more repetitions of a vowel".

The existence of metacharacters poses a problem if you want to create a regular expression (or regex) that matches a
literal metacharacter, such as "$". You can do this by escaping the metacharacters by putting a backslash in front of them.
However, this can cause problems, since backslashes also have an escaping function in normal Python strings.
This can mean putting three or four backslashes in a row to do all the escaping.

To avoid this, you can use a raw string, which is a normal string with an "r" in front of it.
We saw usage of raw strings in the previous lesson.

The first metacharacter we will look at is . (dot).
This matches any character, other than a new line.

"""

# 1

import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")                # Match 1

if re.match(pattern, "gray"):
    print("Match 2")                # Match 2

if re.match(pattern, "blue"):
    print("Match 3")

"""

The next two metacharacters are ^ and $.
These match the start and end of a string, respectively.

"""

# 1

import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")                # Match 1

if re.match(pattern, "gray"):
    print("Match 2")                # Match 2

if re.match(pattern, "stingray"):
    print("Match 3")

"""

The pattern "^gr.y$" means that the string should start with gr, 
then follow with any character, except a newline, and end with y.

"""

"""

Some more metacharacters are *, +, ?, { and }.
These specify numbers of repetitions.
The metacharacter * means "zero or more repetitions of the previous thing". 
It tries to match as many repetitions as possible. The "previous thing" can be a single character, a class, 
or a group of characters in parentheses.

"""

# 2

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")                        # Match 1

if re. match(pattern, "eggspamspamegg"):
    print("Match 2")                        # Match 2

if re.match(pattern, "spam"):
    print("Match 3")

# The example above matches strings that start with "egg" and follow with zero or more "spam"s.

"""

The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to 
"zero or more repetitions".

"""

# 2.1

import re

pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1")                        # Match 1

if re.match(pattern, "ggggggggggggg"):
    print("Match 2")                        # Match 2

if re.match(pattern, "abc"):
    print("Match 3")

"""

To summarize:
* matches 0 or more occurrences of the preceding expression.
+ matches 1 or more occurrence of the preceding expression.

"""

