"""

In Python, the term packaging refers to putting modules you have written in a standard format,
so that other programmers can install and use them with ease.
This involves use of the modules setuptools and distutils.
The first step in packaging is to organize existing files correctly.
Place all of the files you want to put in a library in the same parent directory.
This directory should also contain a file called __init__.py, which can be blank but must be present in the directory.
This directory goes into another directory containing the readme and license, as well as an important file called setup.py.
Example directory structure:

SoloLearn/
   LICENSE.txt
   README.txt
   setup.py
   sololearn/
      __init__.py
      sololearn.py
      sololearn2.py

You can place as many script files in the directory as you need.

"""