# how to define an empty dictionary?
my_dictionary = dict()

# is it really a dictionary? 
#print(type(my_dictionary)) # <class 'dict'>

# is it empty?
#print(len(my_dictionary))  # 0

# create our own dictionary
my_dictionary = {'Kevin': 2}
my_dictionary.update({'Stuart': 1})

#my_dictionary['Bob'] = 2

# what are the built-in methods of dictionaries
#help(dict)
#print(my_dictionary)


my_dictionary.update({'Stuart': 5})
# does it create a pair?
my_dictionary == {'Kevin': 2, 'Stuart': 1, 'Stuart': 5}

# no, it doesn't, if a key exists, then update its value
my_dictionary == {'Kevin': 2, 'Stuart': 5}
#print(my_dictionary)

# how to loop through a dictionary

# 1. loop through its keys
for next_key in my_dictionary:
    print(next_key)

# 2. loop through its values
for next_value in my_dictionary.values():
    print(next_value)

# 3. loop through both its keys and values
for (next_key, next_value) in my_dictionary.items():
    print((next_key, next_value))
