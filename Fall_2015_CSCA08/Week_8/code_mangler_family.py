def code_stealer(file_handle):
    '''(io.TextIOWrapper) -> str
    Return all internal comments.
    '''
    # create an empty result ready for use
    result = ''
    for next_line in file_handle:
        if "#" in next_line:
            result += next_line
    return result


def code_mangler(file_handle):
    '''(io.TextIOWrapper) -> str
    the damn code mangler
    '''
    # create an empty result ready to use
    raw_result = set()
    # count triple quotes
    num_triple_quote = 0
    for next_line in file_handle:
        # avoid descriptions of a function
        if (num_triple_quote % 2) != 1:
            if ('#' not in next_line) and ("'''" not in next_line):
                raw_result.add(next_line)
        if "'''" in next_line:
            num_triple_quote += 1
    # create an empty result string ready for use
    result = ''
    # randomly arrange lines in raw result set
    for next_element in raw_result:
        result += next_element
    return result


if __name__ == "__main__":
    file_name = 'ex6.py'
    file_handle = open(file_name, "r")
    # uncomment to use
    #print(code_stealer(file_handle))
    
    print(code_mangler(file_handle))
    file_handle.close()
