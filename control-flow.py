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
    user_age = input("Please enter your age: ")

    # Define the voting age requirement
    voting_age = 18

    try:
        # Convert input to integer
        age = int(user_age)

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

# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    # Prompt the user for the dog's age
    dog_age = input("Input a dog's age: ")

    try:
        # Convert input to an integer
        age = int(dog_age)

        # Handle invalid negative ages
        if age < 0:
            print("Invalid input! Age cannot be negative.")
        # Logic for first two years
        elif age <= 2:
            dog_years = age * 10
            print(f"The dog's age in dog years is {dog_years}.")
        # Logic for subsequent years
        else:
            # First 2 years = 20 dog years
            # Subsequent years = (age - 2) * 7
            dog_years = 20 + (age - 2) * 7
            print(f"The dog's age in dog years is {dog_years}.")

    except ValueError:
        # Handle non-numerical entries
        print("Invalid input. Please enter a whole number.")

# Call the function
calculate_dog_years()

# Problem 4: Weather advice
#
# Write a Python script named `weather_advice` that provides clothing advice
# based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle
#   multiple conditions.

def weather_advice():
    # .lower() is used to ensure the logic works even if the user types 'YES' or 'Yes'
    is_cold = input("Is it cold? (yes/no): ").lower()
    is_raining = input("Is it raining? (yes/no): ").lower()

    # Determine clothing advice using logical operators
    if is_cold == "yes" and is_raining == "yes":
        print("Wear a waterproof coat.")
    elif is_cold == "yes" and is_raining == "no":
        print("Wear a warm coat.")
    elif is_cold == "no" and is_raining == "yes":
        print("Carry an umbrella.")
    elif is_cold == "no" and is_raining == "no":
        print("Wear light clothing.")
    else:
        # Feedback for invalid entries other than yes/no
        print("Invalid input. Please answer with 'yes' or 'no'.")

# Call the function
weather_advice()
