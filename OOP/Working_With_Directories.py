"""

Object-oriented filesystem paths

https://docs.python.org/3/library/pathlib.html

"""

""" 
Absolute path - working with hard disk's files
c:\Program Files\Microsoft
"""
# Relative path - working with files in current project

#1

from pathlib import Path

path = Path("ecommerce")               """ ecommerce is a current package in the project """
print(path.exists())                   # True

#1.1

from pathlib import Path

path = Path("ecommerce1")             # """ ecommerce1 isn't a current package in the project """
print(path.exists())                  # False

#2

from pathlib import Path

path = Path("emails")                 # """ mkdir() creates emails package in the project """
print(path.mkdir())                   # None

#2.1

from pathlib import Path

path = Path("emails")                 # """ rmdir() removes emails package from the project """
print(path.rmdir())                   # None

#3

from pathlib import Path

path = Path()
for file in path.glob('*.py'):        # """ path.glob('*.py') returns all exists .py files in the project """
    print(file)                       # app.py
    
    
