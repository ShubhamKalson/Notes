class AccessExample:
    def __init__(self):
        # Public attribute
        self.public_attr = "I'm a public attribute"
        
        # Protected attribute
        self._protected_attr = "I'm a protected attribute"
        
        # Private attribute
        self.__private_attr = "I'm a private attribute"

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

# Creating an object
obj = AccessExample()

# Accessing attributes and methods
print(obj.public_attr)          # Public attribute
print(obj._protected_attr)      # Protected attribute (can still be accessed)
# print(obj.__private_attr)     # This will raise an AttributeError
print(obj._AccessExample__private_attr)  
# Private attribute using name mangling
#Name Mangling is used and possible as python never enforces such strict encapsulation like other langauges

obj.public_method()             # Public method
obj._protected_method()         # Protected method
# obj.__private_method()       # This will raise an AttributeError
obj._AccessExample__private_method()      # Private method using name mangling
