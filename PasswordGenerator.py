import random
import string

def password_generator():
    print("Password Generator")
    print("------------------")

    while True:
        password_length = input("Enter the password length (min 8 characters): ")
        if password_length.isdigit() and int(password_length) >= 8:
            password_length = int(password_length)
            break
        else:
            print("Invalid input. Please enter a number greater than or equal to 8.")

    while True:
        use_uppercase = input("Include uppercase letters? (yes/no): ")
        if use_uppercase.lower() in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        use_numbers = input("Include numbers? (yes/no): ")
        if use_numbers.lower() in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        use_special_chars = input("Include special characters? (yes/no): ")
        if use_special_chars.lower() in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    characters = string.ascii_lowercase
    if use_uppercase.lower() == "yes":
        characters += string.ascii_uppercase
    if use_numbers.lower() == "yes":
        characters += string.digits
    if use_special_chars.lower() == "yes":
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(f"Generated password: {password}")

    play_again = input("Do you want to generate another password? (yes/no): ")
    if play_again.lower() == "yes":
        password_generator()
    else:
        print("Thank you!")

password_generator()