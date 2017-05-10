# step 1: basic import
# import week5_import_a
# print(week5_import_a.my_cool_function())

# step 2: giving it a better name
import week5_import_a as imp

# part of step 2
print(imp.my_cool_function())

# part of step 4
print("The name of week5_import_b is: ", __name__)

# step 5: show how main code can be hidden
if(__name__ == "__main__"):
    print("week5_import_b.py is being run as the main file")
