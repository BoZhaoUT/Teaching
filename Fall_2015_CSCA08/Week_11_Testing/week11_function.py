def remove_dup_values(my_dictionary):
    ''' (dict of {int: int}) -> int
    Remove all entries of my dictionary whose values are not unique in the
    dictionary. Return the number of entries that were removed.
    >>> my_dictionary = {}
    >>> remove_dup_values(my_dictionary)
    0
    >>> expected_result = {}
    >>> my_dictionary == expected_result
    True
     
    >>> my_dictionary = {1: 11, 2: 11}
    >>> remove_dup_values(my_dictionary)
    2
    >>> expected_result = {}
    >>> my_dictionary == expected_result
    True
    
    >>> my_dictionary = {1: 20, 2: 30}
    >>> remove_dup_values(my_dictionary)
    0
    >>> expected_result = {1: 20, 2: 30}
    >>> my_dictionary == expected_result
    True
    
    ...
    
    '''
    dictionary_values = list(my_dictionary.values())
    key_delete = []
    count = 0
    for (next_key, next_value) in my_dictionary.items():
        if dictionary_values.count(next_value) > 1:
            key_delete.append(next_key)
            count += 1
    for next_key in key_delete:
        del my_dictionary[next_key]
    return count
 
 
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    '''
    chart
    length    num_dup_entries
    0                0
     
    1                0
     
    2                0
    2                2
     
    3                0
    3                2
    3                3
    
    4                4(2, 2)
    '''