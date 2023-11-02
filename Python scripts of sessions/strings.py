# Diving into string type data type
name = "CODEX"
print (name)            # prints the whole string
print (name[1])         # prints the character at specific index, here "1"
print (name[1:3])       # prints the string from 1st index to 3rd i.e, 2nd character to 4th
print (name[1:])        # prints the whole string from 1st index i.e, 2nd character to last
print (name*2)          # prints the string 2 times
print (name + " ITER")  # prints the string along with the added string
print (name[::-1])      # prints the string in reversed order
print ("The String is",name,"ITER") #printing the string along with other string

# printing sentences
# '\t' : to give tabs
# '\n' : next line
long_string = "\n\nLorem \t ipsum \t dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \n Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print (long_string)

#another way to write long paragraphs in multi line
long_string = """\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n\n"""
print (long_string)


# some other useful built-in string methods
print (name.capitalize())  # capitalizes first letter of string
print (name.upper())       # converts all lowercase letters in string to uppercase
print (name.lower())       # converts all uppercase letters in string to lowercase
print (len(name))         # prints the length of the string


# Sample string for demonstration
sample_string = "Hello, Python!"

# Length of the string
print("Length of the string:", len(sample_string))

# Accessing individual characters
print("First character:", sample_string[0])
print("Last character:", sample_string[-1])

# Slicing the string
print("Slice from index 2 to 5:", sample_string[2:6])

# Concatenating strings
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print("Concatenated string:", concatenated_string)

# String repetition
repeated_string = "Hello" * 3
print("Repeated string:", repeated_string)

# String methods

# Upper and lower case
print("Uppercase:", sample_string.upper())
print("Lowercase:", sample_string.lower())

# Replace characters
print("Replace 'Python' with 'World':", sample_string.replace("Python", "World"))

# Count occurrences of a substring
print("Occurrences of 'l':", sample_string.count("l"))

# Find the index of a substring
print("Index of 'Python':", sample_string.find("Python"))

# Check if the string starts or ends with a particular substring
print("Starts with 'Hello':", sample_string.startswith("Hello"))
print("Ends with 'World':", sample_string.endswith("World"))

# Splitting the string into a list of substrings
print("Splitting the string by comma:", sample_string.split(","))

# Stripping leading and trailing whitespaces
whitespace_string = "    This is a string with whitespaces.   "
print("Original string:", whitespace_string)
print("Stripped string:", whitespace_string.strip())

# Checking if the string contains only alphabetic characters
alpha_string = "HelloPython"
print("Is 'alpha_string' alphabetic?", alpha_string.isalpha())

# Checking if the string contains only numeric characters
numeric_string = "12345"
print("Is 'numeric_string' numeric?", numeric_string.isnumeric())

# Checking if the string contains only alphanumeric characters
alphanumeric_string = "Hello123"
print("Is 'alphanumeric_string' alphanumeric?", alphanumeric_string.isalnum())

# Checking if the string is in title case (words start with uppercase letters)
title_case_string = "This Is A Title"
print("Is 'title_case_string' in title case?", title_case_string.istitle())

# Checking if the string contains only whitespace characters
whitespace_string = "    "
print("Is 'whitespace_string' whitespace?", whitespace_string.isspace())
