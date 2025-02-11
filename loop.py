import random

# Set the secret_number variable here (between 1 and 10)
# Initialize the guess variable here with a value of 0

secret_number = 9
guess = 0

while guess != secret_number:  # Add the while loop condition here
	guess = random.randint(1, 10)
	print(f"Guessing: {guess}")

print(f"I guessed the right number! It was {secret_number}")

for i in range(1, 11):
  print(i)

valid_input = False
while not valid_input:
  user_input = input("Please enter a number greater than 0: ")
  if user_input > 0:
    valid_input = True
  else:
    print("Invalid input. Please try again.")

player_score = 80

if player_score > 100:
  print("Congratulations! You scored over 100 points.")
else:
  print("Keep trying to beat your high score!")