"""Clean Code in Python - Chapter 3: General Traits of Good Code

> Functions and arguments
Can be used for implementing changes in existing methods:
result = first_function(1, c=2, new_implementation=True)  # use kwarg to change behavior
"""


def first_function(a, *, c):
    """A function with a required argument (a) and a keyword-only argument (c)"""
    print(a, c)


def second_function(a, *arg, c):
    """A function with a required argument (a) and a keyword-only argument (c)
    And the ability to take any number of positional arguments after a (implemented by *arg)"""
    print(a, *arg c)


'''
>>> first_function(1, c=10)
1 10
>>> second_function(1, 2, 3, 4, c=10)
1 2 3 4 10
'''
