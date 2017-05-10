# week 7, more recursion
# no slides for this week





# today's plan
# 1: is_near_palindrom
# 2: ex 5
# 3: quiz 3





def is_palindrome(my_str):
    ''' (str) -> bool
    Return True iff my_str is a palindrome.
    >>> is_palindrome("")
    True
    >>> is_palindrome("radar")
    True
    >>> is_palindrome("nick")
    False
    '''
    # base case
    if len(my_str) <= 1:
        result = True
    # recursive case
    elif my_str[0] == my_str[-1]:
        result = is_palindrome(my_str[1:-1])
    # base case
    else:
        result = False
    return result


# at most one pair of letters can be different


def is_near_palindrome(my_str):
    ''' (str) -> bool
    Return True iff my_str is a near palindrome.
    >>> is_near_palindrome("radar")
    True
    >>> is_near_palindrome("naval")
    True
    >>> is_near_palindrome("nick")
    False
    '''
    # base case
    if len(my_str) <= 1:
        result = True
    # recursive case
    elif my_str[0] == my_str[-1]:
        result = is_near_palindrome(my_str[1:-1])
    # recursive case
    else:
        result = is_palindrome(my_str[1:-1])
    return result


# we can set how many pairs of letters can be different

def is_palindrome_helper(my_str, num_changes):
    ''' (str, int) -> bool
    Return True iff my_str is within num_changes of being a palindrome.
    REQ: num_chamges >= 0
    >>> is_palindrome_helper("radar", 0)
    True
    >>> is_palindrome_helper("naval", 1)
    True
    >>> is_palindrome_helper("palindrome", 4)
    False
    >>> is_palindrome_helper("palindrome", 5)
    True
    '''
    # base case
    if len(my_str) <= 1:
        result = True
    # recursive case
    elif my_str[0] == my_str[-1]:
        result = is_palindrome_helper(my_str[1:-1], num_changes)
    # recursive case
    elif num_changes > 0:
        result = is_palindrome_helper(my_str[1:-1], num_changes - 1)
    # base case
    else:
        result = False
    return result


# note: this is not a good function name
def is_near_palindrome_op(my_str, num_changes=1):
    ''' (str, int) -> bool
    Return True iff my_word is within num_changes of being a palindrome.
    REQ: num_changes >= 0
    >>> is_near_palindrome_op("naval", 1)
    True
    >>> is_near_palindrome_op("naval")
    True
    >>> is_near_palindrome_op("palindrome", 4)
    False
    >>> is_near_palindrome_op("palindrome", 5)
    True
    '''
    # base case
    if len(my_str) <= 1:
        result = True
    # recursive case
    elif my_str[0] == my_str[-1]:
        result = is_near_palindrome_op(my_str[1:-1], num_changes)
    # recursive case
    elif num_changes > 0:
        result = is_near_palindrome_op(my_str[1:-1], num_changes - 1)
    # base case
    else:
        result = False
    return result


# ex5
def rmax(my_list):
    ''' (list of int) -> int
    Return the largest integer in my_list.
    REQ: my_list contains at least one integer
    >>> rmax([2])
    2
    >>> rmax([1, 4])
    4
    >>> rmax([0, -2, 5])
    5
    >>> rmax([-1, 0, 0, -1])
    0
    '''
    # base case
    if len(my_list) == 1:
        result = my_list[0]
    # recursive case
    else:
        # find the largest integer in the rest of my_list
        max_in_sub_list = rmax(my_list[1:])
        # find the largest itneger in my_list
        if my_list[0] < max_in_sub_list:
            result = max_in_sub_list
        else:
            result = my_list[0]
    return result


# note: this is not a good function name
def rmax_op(my_list, largest_int=-float("inf")):
    ''' (list of int, int) -> int
    Return the largest integer in my_list.
    REQ: my_list contains at least one integer
    >>> rmax_op([2])
    2
    >>> rmax_op([1, 4])
    4
    >>> rmax_op([0, -2, 5])
    5
    >>> rmax_op([-1, 0, -1])
    0
    '''
    # update largest_int if a new largest integer is found
    if my_list[0] > largest_int:
        largest_int = my_list[0]
    # base case
    if len(my_list) == 1:
        result = largest_int
    # recursive case
    else:
        result = rmax_op(my_list[1:], largest_int)
    return result


def second_smallest(my_list, s_int=float("inf"), second_s_int=float("inf")):
    ''' (list of int, int, int) -> int
    Return the second smallest integer in my_list.
    REQ: my_list contains at least two integers
    >>> second_smallest([2, 3, 0])
    2
    >>> second_smallest([1, 0])
    1
    >>> second_smallest([-4, 3, 0, 10, -8])
    -4
    '''
    # update the smallest integer s_int and 
    # the second smallest integer second_s_int
    if my_list[0] < s_int:
        second_s_int = s_int
        s_int = my_list[0]
    elif my_list[0] < second_s_int:
        second_s_int = my_list[0]
    # base case
    if len(my_list) == 1:
        result = second_s_int
    # recursive case
    else:
        result = second_smallest(my_list[1:], s_int, second_s_int)
    return result


def sum_max_min(my_list, max_int=-float("inf"), min_int=float("inf")):
    ''' (list of int, int, int) -> int
    Return the sum of the largest and the smallest integer in my_list.
    REQ: my_list contains at least one integer
    >>> sum_max_min([1, 0])
    1
    >>> sum_max_min([3])
    6
    >>> sum_max_min([0, -3, 2, 5])
    2
    '''
    # update the largest intger max_int and 
    # the smallest integer min_int
    if my_list[0] > max_int:
        max_int = my_list[0]
    if my_list[0] < min_int:
        min_int = my_list[0]
    # base case
    if len(my_list) == 1:
        result = max_int + min_int
    # recursive case
    else:
        result = sum_max_min(my_list[1:], max_int, min_int)
    return result










# quiz 3
