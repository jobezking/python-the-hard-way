# Step 1: Starter code: function with 2 parameters: word_to_count and sentence (provided)
def get_word_count(word_to_count, sentence):
    # Step 2: Split the sentence into words
    # HINT: Use a method called split
    words = sentence.split()
    # Step 3: Initialize the count variable
    count = 0
    # Step 4: Use a for loop to iterate over the words and count occurrences
    for word in words:
        if word == word_to_count:
            count += 1
    # Step 5: Print the result
    print(f"The word '{word_to_count}' appears {count} times in the sentence.")

word_to_count = "happy"
sentence = "In a happy home, a happy heart creates a happy space."
# This will call the created function
get_word_count(word_to_count, sentence)

numbers = [3, 9, 1, 10, 5, 2, 8]

### Your code here
for number in numbers:
    if number%2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

#this DOES NOT alter the list!!!
books = ["Book A", "Book B", "Book C"]

target_book = "Book B"

for book in books:
    if book == target_book:
        print(f"{target_book} found")
        book = "checked out"
    else:
        continue
print(books)

#to update the list!
books = ["Book A", "Book B", "Book C"]

target_book = "Book B"

for i in range(len(books)):
  if books[i] == target_book:
    print(f"{target_book} found")
    books[i] = "checked out"
    break

print(books) 