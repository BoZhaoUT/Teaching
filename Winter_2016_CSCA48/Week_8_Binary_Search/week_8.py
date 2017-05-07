# week 8, binary search






# today's plan
# 1: binary_search
# 2: ex 6 (solution)
# 3: quiz 3 (solution)



def binary_search(L, s):
    '''(list of int, int) -> bool
    Return True iff s is an element of L, otherwise False
    REQ: L must be sorted in increasing order 
    >>> binary_search([-5, 3, 4, 5, 7], 4)
    True
    >>> binary_search([], 3)
    False
    >>> binary_search([1, 2, 4, 5], 5)
    True
    >>> binary_search([4, 10, 11], 5)
    False
    '''
    # BASE CASE: If L is empty, it's not in the list
    if L == []:
        result = False
    # RECURSIVE DECOMP: Pick the middle element, if we found
    # what we're looking for, great. If not, then we've at
    # least cut the list in half
    else:
        # get the middle element of the list
        midpoint = len(L) // 2
        median = L[midpoint]
        # if we found it, then we can stop
        if s == median:
            result = True
        # if we didn't find it, then see whether we need to continue searching
        # in the left side of the list, or the right
        elif s < median:
            result = binary_search(L[:midpoint], s)
        else:
            result = binary_search(L[midpoint+1:], s)
    return result


# restore internal comments
def binary_search2(L, s):
    '''(list of int, int) -> int
    Return the index of s in the list L, or -1 if s is not in L
    REQ: L must be sorted in increasing order 
    '''
    # 
    if L == []:
        result = -1
    else:
        # 
        midpoint = len(L) // 2
        median = L[midpoint]
        if s == median:
            # 
            result = midpoint
        elif s < median:
            #
            result = binary_search2(L[:midpoint], s)
        else:
            # 
            result = binary_search2(L[midpoint+1:], s)
            # 
            if result != -1:
                result += midpoint + 1
    return result

def binary_search2(L, s):
    '''(list of int, int) -> int
    Return the index of s in the list L, or -1 if s is not in L
    REQ: L must be sorted in increasing order 
    '''
    # BASE CASE: If L is empty, return -1
    if L == []:
        result = -1
    else:
        # GENERAL CASE
        # Get the middle value of L, if it's larger than s, then s must be in
        # the first half of the list, so call binary_search on the first half,
        # otherwise, call it on the second half of L, if it's equal to s, then
        # we've found s and we can stop
        midpoint = len(L) // 2
        median = L[midpoint]
        if s == median:
            # found it. return its index
            result = midpoint
        elif s < median:
            # if s is in L, it must be in the first half of the list
            # so just perform a binary search on the first half of the list
            # and return that search's result
            result = binary_search2(L[:midpoint], s)
        else:
            # if s is in L, it must be in the latter half of the list
            # so perform a binary search on the latter half of the list,
            # however, this time, if we do get a result, we have to return
            # its offset from our current midpoint
            result = binary_search2(L[midpoint+1:], s)
            # if we didn't find it, just pass on the -1, but if we did
            # we have to add the index in the right list to the index of
            # our middle element to get its index in our list
            if result != -1:
                result += midpoint + 1
    return result


def binary_search3(L, s):
    '''(list of int, int) -> int
    Return the index of s in the list L, or -1 if s is not in L
    REQ: L must be sorted in increasing order
    '''
    if L == []:
        result = -1
    else:
        result = binary_search3_helper(L, s, 0, len(L)-1)
    return result


def binary_search3_helper(L, s, start, end):
    # Base Case: One item list, start=0, end=0
    # If that element is the one we're looking for return its index otherwise return -1
    if start == end:
        if s == L[start]:
            result = start
        else:
            result = -1
    # recursive decomposition:
    else:
        midpoint = (start + end) // 2
        median = L[midpoint]
        # 3 cases, the element in the middle is the one we're looking for
        if s == median:
            result = midpoint
        # the middle element is greater than the value for which we're
        # searching, so look to the left
        elif s < median:
            result = binary_search3_helper(L, s, start, midpoint)
        # the middle element is smaller than the value for which were
        # searching, so look to the right
        else:
            result = binary_search3_helper(L, s, midpoint+1, end)
    return result


def binary_search4(L, s):
    '''(list of float) -> int
    Return the index of s in the list L, or -1 if s is not in L
    REQ: L must be a sorted list
    '''
    start = 0
    end = len(L) - 1
    found = False
    result = -1
    while not found and start <= end:
        midpoint = (start + end) // 2
        median = L[midpoint]
        # the element in the middle is the one we're looking for
        if s == median:
            found = True
            result = midpoint
        else:
            # the middle element is greater than the value for which we're
            # searching, so look to the left            
            if s < median:
                end = midpoint - 1
            # the middle element is smaller than the value for which were
            # searching, so look to the right            
            else:
                start = midpoint + 1
    return result


if(__name__ == "__main__"):
    L = [1, 2, 4, 6, 8, 10, 12, 13, 15, 17, 19, 20, 25]
    print(binary_search([], 3))
    print(binary_search(L, 3))
    print(binary_search(L, 15))

    print(binary_search2([], 3))
    print(binary_search2(L, 3))
    print(binary_search2(L, 15))

    print(binary_search3([], 3))
    print(binary_search3(L, 3))
    print(binary_search3(L, 15))

    print(binary_search4([], 3))
    print(binary_search4(L, 3))
    print(binary_search4(L, 15))
