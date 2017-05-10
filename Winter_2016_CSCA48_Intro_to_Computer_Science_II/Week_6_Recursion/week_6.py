# week 6, recursion
# no slides for this week





# today's plan
# 1: 
# 2: example
# 3: term test 1
# 4: ex5 (if we have time)





# first 10 Fibonacci numbers
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55


def fib(n):
    ''' (int) -> int
    Return the nth Fibonacci number.
    REQ: n >= 0
    >>> fib(1)
    1
    >>> fib(2)
    2
    >>> fib(4)
    5
    '''
    # base case
    if (n < 2):
        result = 1
    # recursive case
    else:
        n_minus_1_term = fib(n - 1)
        n_minus_2_term = fib(n - 2)
        result = n_minus_1_term + n_minus_2_term
    return result
    







# summary

# Recursion needs at least 1 base case
# Recursion needs at least 1 recursive case
# Base cases should be as simple as possible - Brian
# Python Tutor: course webpage -> course software










# term test 1

# No remark request if you leave this room with your term test.
# If you suspect there is a marking mistake, then
#     write down the description of it on the front page.









# ex5

# 1. Don't change an input list unless you're told to
# Suppose you're asked to calculate the average age of all
# course instructors at UTSC, and there's a list of ages
# in the university's database. 
# Q: Do you want to mutate the list each time you do the calculation? 

# don't use pop, remove, sort, del, reverse ...












# 2. Try to be efficient
# From the handout:
#     You should also try to be efficient. In particular, no function
# should ever need to acces any element of the lsit more than once.
# 
# using rmin and rmax will go through the entire list twice. FROBIDDEN









# 3. Optional parameters are you best friends
# see the example below



def rmin(my_list, smallest_int=float("inf")):
    ''' (list of int, int) -> int
    Return the smallest integer in my_list.
    REQ: my_list contains at least one integer
    >>> rmin([2])
    2
    >>> rmin([1, 4])
    1
    >>> rmin([0, -2, 5])
    -2
    >>> rmin([-1, 0, -1])
    -1
    '''
    # update smallest_int if a new smallest integer is found
    if my_list[0] < smallest_int:
        smallest_int = my_list[0]
    # base case
    if len(my_list) == 1:
        result = smallest_int
    # recursive case
    else:
        result = rmin(my_list[1:], smallest_int)
    return result
