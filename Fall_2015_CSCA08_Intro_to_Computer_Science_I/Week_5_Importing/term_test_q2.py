def func1(var1, var2):
    print("func1: ", var1, var2)
    return var3

def func2(var1, var2):
    var3 = func1(var1, var2)
    print("func2: ", var1, var2, var3)
    return var1 + var2

def func3(var1 ,var2 ,var3):
    var1 = func2(var1, var2)
    var2 = func2(var2, var3)
    print("func3: ", var1, var2, var3)
    return func2(func1(var1, var2), func1(var2, var1))

var1 = "A"
var2 = "B"
var3 = "C"
print("STEP 1: ", var1, var2, var3)
var3 = func1(var1, var2)
print("STEP 2: ", var1, var2 ,var3)
var1 = "A"
var2 = "B"
var3 = "C"
var3 = func2(var1, var2)
print("STEP 3: ", var1, var2, var3)
var1 = "A"
var2 = "B"
var3 = "C"
var3 = func3(var1, var2, var3)
print("STEP 4: ", var1, var2, var3)
