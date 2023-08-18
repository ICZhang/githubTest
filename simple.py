
#This is a comment

"""
This is also a comment
"""


x = 2

def myfunc():
  global x
  x = 21

myfunc()
print(x)

for x in range(7):
    if x < 6:
        print(x)
    else:
        break


example = [1, 2, "panda"]

print(example[2])

example.append(4)
example.remove(1)

print(example)

def example(tree1, flower2):
    print(tree1, flower2)

example("oak", "rose")

import numpy
import pandas

