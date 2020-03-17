# *********************************************
# NEVER DO THIS, BUT... it is recursion

# def my_recursion(n):
#     print(n)
#     my_recursion(n+1)

# my_recursion(1)
# *********************************************

# we have now added a base case to prevent infinite recursion


def my_recursion(n):
    print(n)
    if n == 5:
        return
    my_recursion(n + 1)


my_recursion(1)

"""call stack order
1. on line 21, we call my_recursion with the value of 1
2. go into the my_recursion function, and on line 15, print n, return and remove it from the stack
3. does n == 5? no, so we go to the line 18 and call my_recursion with the value of 2 (1 + 1)
4. then we go back into the function with the value of n being 2, print n, return and remove it from the stack
5. I think you see where this is going, and going, and going, and go....

from the wise Don: "So for visual purposes, once we have called the base case, the stack crumbles to the ground in the reverse order of calls"
"""


def my_recursion(n):
    print(n)
    if n == 3:
        return
    my_recursion(n + 1)
    my_recursion(n + 1)


my_recursion(1)

"""call stack order
*** PLUG THIS FUNCTION ABOVE INTO http://pythontutor.com/visualize.html#mode=edit
1. start with my_recursion(1)
add and remove print()
2. on line 37 we call my_recursion() with a value of 2
and that prints() then removes the print
3. it equals 3 and removes it from the call stack
4. then we call on line 38 my_recursion() with the value of 3

"""
