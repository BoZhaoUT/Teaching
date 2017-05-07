def remove_dup_values(my_dictionary):
    ''' (dict of {int: int}) -> int
    Remove all entries of my dictionary whose values are not unique in the
    dictionary. Return the number of entries that were removed.
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    # detail implementation
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
