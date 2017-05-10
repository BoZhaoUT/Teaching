
def inverting(input_dict):
    '''(dict) -> dict
    Return an inverted copy of input_dict. Every key-value pair in input_dict
    will be a value-key pair in the result. Since multiple values in
    input_dict may be mapped to by the same key, the values in the returned
    dictionary will be held as a set.
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
    for (next_key, next_value) in input_dict.items():
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
