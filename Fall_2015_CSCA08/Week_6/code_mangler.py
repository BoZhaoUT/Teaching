def code_mangler(file_handle):
    '''(io.TextIOWrapper) -> str
    Remove indentations, shuffle all the code and headers.
    '''
    # create an empty result ready to use
    raw_result = set()
    # count triple quotes
    num_triple_quote = 0
    # loop through given file
    for next_line in file_handle:
        # avoid descriptions of a function
        if (num_triple_quote % 2) != 1:
            # avoid internal comments and quotatiosn marks
            if ('#' not in next_line) and ("'''" not in next_line):
                # remove indentations
                next_line = next_line.lstrip()
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
    file_name = 'ex4.py'
    file_handle = open(file_name, "r")
    print(code_mangler(file_handle))
    file_handle.close()
