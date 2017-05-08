def func_0(var1):
    var1 = 'A'
    print(var1)

def func_1(var1,var2):
    var1 = 'B'
    var2 = 'C'
    print(var1, var2)
    return var2

var1 = 'X'
var2 = 'Y'
print(var1, var2)
var1 = func_0(var2)
print(var1, var2)
var1 = func_1(var1, var2)
print(var1, var2)
