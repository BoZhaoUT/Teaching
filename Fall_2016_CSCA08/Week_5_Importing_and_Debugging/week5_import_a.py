def my_cool_function():
    return "I wrote this in the file: week5_import_a.py"

# step 3: show that the file gets run, which means global code gets run
print("Hey look... this gets printed when I get imported")

# step 4: talk about wanting to "hide" global code from importing file
# (especially the automarker). Maybe there's a built-in variable we can use
print("The name of week5_import_a.py is: ", __name__)

# step 5: show how main code can be hidden
if(__name__ == "__main__"):
    print("week5_import_a.py is being run as the main file")

