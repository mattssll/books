Chapter 03 - General traits of good code
========================================
This directory contains the examples for chapter 3 of the book.


Testing
-------
To run the tests for this chapter, issue the following command::

    make test


<ul>Error Handling</ul>
<li>Value Substitution</li>
<li>Error Logging</li>
<li>Exception Handling</li>

Assertions - example of code: assert(x == y, "x and y are not equal")
cohesion and coupling: the lower the cohesion the higher the coupling
ripple effects: when a change in one part of the code causes a change in another part of the code
DRY/OAOO (Don't repeat yourself/Once and only once)
YAGNI: You aren't going to need it
KISS: Keep it simple, stupid
EAFP: Easier to ask for forgiveness than permission (try/except)
LBYL: Look before you leap (validating with if for example before doing something)
EAFP and LBYL are kind of opposite
Inheritance: is-a relationship, good uses (specialization): add different behaviour from parent (base), interfaces, exceptions
Anti Pattern for Inheritance: Inherit from Dictionary instead of simply composing data attribute with it - too many non needed methods in Dict class def - Class has a dict, is not a dict
Multiple Inheritance introduces the diamond problem in many languages, in python it's ok to do it though (with care)
Diamond Problem: when a class inherits from two classes that inherit from the same class (inherits the same two times)
Composition: has-a relationship, good uses: add different behaviour from parent (base), interfaces, exceptions
Mixins make use of multiple inheritance - a mixin is a class that is not meant to be instantiated on its own, but to be inherited from - gives additional functionality (attrs, or methods)
Functions and parameters: After a keyword arg is passed the next args must be keyword args
positional arguments are passed by position, keyword arguments are passed by name
positional only arguments: added in py 3.8 - can only be passed by position, not by name, "/" is used to separate them from the rest of the args
keyword only arguments: added in py 3.8 - can only be passed by name, not by position, "*"  is used to separate them from the rest of the args (and "*args if we want to let pass more positional args)
we should in 99.9% of the cases use keyword arguments as they have better readability
Packing and Unpacking Values: *args, **kwargs - *args is 1d, **kwargs is a dict
Orthogonality: the ability to combine different parts of the code in different ways (changing one do not affect the other)
Two vectors are Orthogonals when they are independent of each other































































