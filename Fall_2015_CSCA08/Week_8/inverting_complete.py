# 1st implementation
def inverting(given_dictionary):
    '''(dict) -> dict
    Return a new dictionary with inverted key-value pairs in given dictionary.
    REQ: values in given dictionary must be immutable
    >>> inverting({})
    {}
    >>> inverting({"Brian": 32})
    {32: {'Brian'}}
    >>> inverting({"Brian": 32, "Paco": 32, "Anya": 22})
    {32: {'Brian', 'Paco'}, 22: {'Anya'}}
    '''
    # create an empty result dictionary ready for use
    result = dict()
    # loop through key-value pairs in the given dictionary
    for (next_key, next_value) in given_dictionary.items():
        # 2 cases to deal with here
        if next_value in result:
            # case1: a key in result dictionary exists, add key in the given
            #         dictionary to the key in result dictionary
            result[next_value].add(next_key)
        else:
            # case2: a key in result dictionary doesn't exist, create a new
            #         key-value pair in result dictionary
            result[next_value] = {next_key}
    return result


# 2nd implementation
def inverting_(given_dictionary):
    '''(dict) -> dict
    Return a new dictionary with inverted key-value pairs in given dictionary.
    REQ: values in given dictionary must be immutable
    >>> inverting({})
    {}
    >>> inverting({"Brian": 32})
    {32: {'Brian'}}
    >>> inverting({"Brian": 32, "Paco": 32, "Anya": 22})
    {32: {'Brian', 'Paco'}, 22: {'Anya'}}
    '''
    # create an empty result dictionary ready for use
    result = dict()
    # loop through key-value pairs in the given dictionary
    for (next_key, next_value) in given_dictionary.items():
        # inverting key-value pair
        result[next_value] = (result.get(next_value, set())).union({next_key})
    return result
