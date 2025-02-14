numerator = 7
denominator = 0

try:
    result = numerator / denominator
    # this line might raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

try:
    file = open("data.txt", "r")
    # Process the file contents here
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: You do not have permission to access this file.")

#Common Errors

# ZeroDivisionError
# FileNotFoundError
# TypeError: trying to perform an operation on incompatible types
# ValueError: trying to pass an inappropriate value to a function
# IndexError: trying to access a list or sequence element that is out of bounds
# ImportError: raised when an imported module or package cannot be found
# KeyError: raised when a dictionary key is not found
# AttributeError: raised when an attribute reference or attribute assignment fails
# SyntaxError: raised if there is a syntax error in code
