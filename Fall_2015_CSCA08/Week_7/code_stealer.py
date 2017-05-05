def code_stealer(file_handle):
    '''(io.TextIOWrapper) -> str
    Return all internal comments.
    '''
    # create an empty result ready for use
    result = ""
    for next_line in file_handle:
        # leave all internal comments
        if "#" in next_line:
            result += next_line
        # otherwise insert an empty line
        else:
            result += "\n"
    return result


if __name__ == "__main__":
    file_name = 'ex5.py'
    file_handle = open(file_name, "r")
    print(code_stealer(file_handle))
    file_handle.close()
