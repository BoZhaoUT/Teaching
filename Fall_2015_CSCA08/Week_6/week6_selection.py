def ph_value_message(ph_value):
    '''(float) -> str
    Return a message of given ph_value. If a ph value is less
    than 2 or greater than 11, then return "run". If ph_value is
    between 2 and 5, then return "That's pretty acidic, I wouldn't 
    drink it". If ph_value is 5 and 7, then return "Your water is 
    acidic, but you're probably okay". If ph_value is 7, then return
    "Your water is neutral". If ph_value is between 7 and 11, then 
    return "That's pretty basic stuff".
    >>> ph_value(6.0)
    "Your water is acidic, but you're probably okay"
    >>> ph_value(7.0)
    "Your water is neutral"
    >>> ph_value(8.0)
    "That's pretty basic stuff"
    >>> ph_value(0.9)
    "RUN"
    >>> ph_value(2.0)
    "Your water is acidic, but you're probably okay"
    >>> ph_value(12.2)
    "RUN"
    '''
    if (ph_value < 7):
        if (ph_value > 5):
            result = "Your water is acidic, but you're probably okay"
        else:
            if(ph_value < 2):
                result = "RUN!"
            else:
                result = "That's pretty acidic, I wouldn't drink it"
    elif (ph_value > 7):
        if (ph_value > 11):
            result = "RUN!"
        else:
            result = "That's pretty basic stuff"
    elif (ph_value == 7):
        result = "Your water is neutral."
    else:
        result = "Not a valid PH!"
    return result


# a better approach
def ph_value_message(ph_value):
    '''(float) -> str
    Return a message of given ph_value. If a ph value is less
    than 2 or greater than 11, then return "run". If ph_value is
    between 2 and 5, then return "That's pretty acidic, I wouldn't 
    drink it". If ph_value is 5 and 7, then return "Your water is 
    acidic, but you're probably okay". If ph_value is 7, then return
    "Your water is neutral". If ph_value is between 7 and 11, then 
    return "That's pretty basic stuff".
    >>> ph_value(6.0)
    "Your water is acidic, but you're probably okay"
    >>> ph_value(7.0)
    "Your water is neutral"
    >>> ph_value(8.0)
    "That's pretty basic stuff"
    >>> ph_value(0.9)
    "RUN"
    >>> ph_value(2.0)
    "Your water is acidic, but you're probably okay"
    >>> ph_value(12.2)
    "RUN"
    '''    
    if (ph_value < 2):
        result = "RUN"
    elif (ph_value < 5):
        result = "That's pretty acidic, I wouldn't drink it"
    elif (ph_value < 7):
        result = "Your water is acidic, but you're probably okay"
    elif (ph_value == 7):
        result = "Your water is neutral."
    elif (ph_value < 11):
        result = "That's pretty basic stuff"
    else:
        # assume that ph_value is >= 11 here
        result = "RUN"
    return result
