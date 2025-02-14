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