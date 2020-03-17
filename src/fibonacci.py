# fibonacci

# 0, 1 - Base - if we solve this recursively, move towards the base case

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,

# 10th fib number?

# 9th fib + 8th fib

# 9th fib?

# 8th plus 7th

# base case??? 1 and/or 0

# print the nth fib number


def recursive_fib(n):
    # base case
    # test for negatives (TODO)
    # if n is 0
    if n == 0:
        return 0
    # return 0
    # if n is 1
    if n == 1:
        return 1
    # return 1
    # elif we are not on the base case
    # return recursion of n-1 + n -2
    return recursive_fib(n-1) + recursive_fib(n-2)


print(recursive_fib(5))

# the second recursion doesn't hit until the first recursion reaches the base case
# O(2**n)
