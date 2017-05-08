#and functions within functions
def func_a(x):
    x = x + 7
    print(x)
    return x

def func_b(x):
    x = x + func_a(x)
    print(x)
    return x

def func_c(x):
    x = x + func_b(x)
    print(x)
    return x

y = func_c(3)
print(y)