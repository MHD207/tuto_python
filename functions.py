from pathlib import PurePosixPath
from unicodedata import name


def people(name, salary):
    print('your name is ' + name + ' and your salary is ' + salary)

people(input('enter your name '), input('enter your salary  ' + str(name) + '\n'))