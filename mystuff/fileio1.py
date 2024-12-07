test_file = "test.txt"

try:
    with open(test_file, 'r') as file:
        # Read the lines of the file
        file_content = file.read()
        print("File Content:\n", file_content)
        file.close()

except FileNotFoundError:
    print(f"File '{test_file}' not found")
except Exception as e:
    print(f"An error occurred: {e}")