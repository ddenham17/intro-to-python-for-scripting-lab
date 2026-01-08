# Problem 0: Example
#
# This is a practice problem to help you understand how to write code in a 
# provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting
# message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

"""
def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()
"""

# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():
    # Capture user input
    letter = input("Enter a letter (a-z or A-Z): ")

    # Check if the input is a single alphabetical character
    if len(letter) == 1 and letter.isalpha():
        # Convert to lowercase to handle both cases uniformly
        lower_letter = letter.lower()
        
        # Define vowels
        vowels = "aeiou"

        # Determine if it is a vowel or consonant using the 'in' operator
        if lower_letter in vowels:
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input! Please enter a single alphabetical letter.")

# Call the function
check_letter()

# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    # Prompt user for input
    user_input = input("Please enter your age: ")

    # Define the voting age requirement
    voting_age = 18

    try:
        # Convert input to integer
        age = int(user_input)

        # Validate that age is not negative
        if age < 0:
            print("Invalid input! Age cannot be a negative number.")
        # Check eligibility
        elif age >= voting_age:
            print("You are eligible to vote!")
        else:
            print(f"You are not eligible to vote yet. You must be at least {voting_age} years old.")
            
    except ValueError:
        # Handle cases where input is not a whole number (e.g., text or symbols)
        print("Invalid input. Please enter a valid numerical age.")

# Call the function
check_voting_eligibility()