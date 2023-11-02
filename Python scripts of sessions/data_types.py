'''
    There are mainly 5 categories of data type: Numbers, Strings, Lists, Tuples, Dictionaries
'''

#assigning value to variables

x = 25          # integer type
y = 50.25       # floating type
name = "codex"  # string type

print (x)
print (y)
print (name)

# to know which data type the variables are use predefined function type()
# print (type(variable_name))

print ("variable x is",type(x))
print ("variable y is",type(y))
print ("variable name is",type(name))


1. Mutable Data Types:
Mutable data types are those whose values can be modified after creation. 

a. Lists: Lists are ordered collections that can store multiple elements of different data types. You can modify the elements in a list, add new elements, or remove existing elements.

my_list = [1, 2, 3]
my_list[0] = 100  # Modifying
my_list.append(4)  # Adding 
my_list.remove(2)  # Removing
print(my_list) 

b. Dictionaries: Dictionaries are unordered collections that store key-value pairs. You can modify the values associated with keys, add new key-value pairs, or remove existing pairs.

my_dict = {"name": "John", "age": 30}
my_dict["age"] = 31  # Modifying
my_dict["city"] = "New York"  # Adding
del my_dict["name"]  # Removing
print(my_dict)

2. Immutable Data Types:
Immutable data types are those whose values cannot be changed after creation. 
If you want to modify an immutable object's value, you must create a new object with the changes.
a. Strings: Strings represent sequences of characters and are immutable in Python.

my_string = "Hello"
# my_string[0] = "h"  # TypeError: 'str' object does not support item assignment

b. Tuples: Tuples are ordered collections similar to lists but are immutable.

my_tuple = (1, 2, 3)
# my_tuple[0] = 100  # TypeError: 'tuple' object does not support item assignment

c. Numbers (int, float, complex): Numeric data types are also immutable in Python.
my_number = 42
new_number = my_number + 10

