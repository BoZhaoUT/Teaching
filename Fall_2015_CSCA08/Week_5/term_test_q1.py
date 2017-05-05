def add(x, y):
    print("ADD: " + str(x) + " + " + str(y))
    return x + y

def multiply(x, y):
    print("MULT: " + str(y) + " * " + str(x))
    return x * y

def mystery_1(x, y):
    x = x + y
    y = y + x
    print("Mystery 1: " + str(x) + " , " + str(y))
    return y

def mystery_2(x, y):
    x = mystery_1(add(x, y), multiply(x, y))
    print("Mystery 2: " + str(x) + " , " + str(y))
    return x + y

x = 1
y = 2
print("STEP 1: " + str(add(x, y)))
print("STEP 2: " + str(multiply(x, y)))
print("STEP 3: " + str(mystery_1(x, y)))
print("STEP 4: " + str(mystery_2(x, y)))
print("STEP 5: " + str(mystery_2(mystery_1(x, y), x)))
