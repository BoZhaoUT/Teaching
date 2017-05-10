#now let's try functions
def my_function(x):
    y = x+7
    print(y)
    return "Hello"

y = my_function(3)
print(y)

#now more functions
def func_a():
    x = 7

def func_b():
    x = 7
    return x

def func_c(x):
    x = 7

def func_d(x):
    return x

y = func_a()
print(y)
y = func_b()
print(y)
x = 10
y = func_c(x)
print(x, y)
y = func_d(x)
print(x, y)