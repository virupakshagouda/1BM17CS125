



import string
from random import randint
str1=string.printable
for i in range(6):
    print(str1[randint(1,100)],end="")
