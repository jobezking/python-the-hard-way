#"x" - Create - will create a file, returns an error if the file exists
#"a" - Append - will create a file if the specified file does not exists
#"w" - Write - will create a file if the specified file does not exists

test_file = "test.txt"

try:
    with open(test_file, 'r') as file:
        # Read the lines of the file
        pass

except FileNotFoundError:
    print(f"File '{test_file}' not found")
except PermissionError:
    print("You don't have permission to access this file.")    
except Exception as e:
    print(f"An error occurred: {e}")

file = open(test_file, 'r')
file_content = file.read()
test_file_processed = open("debug.log", "x")
print("File Content:\n", file_content)
file.close()