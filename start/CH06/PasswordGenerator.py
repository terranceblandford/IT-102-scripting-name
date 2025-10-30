#PasswordGenerator
#BY Terrance Blandford

import random
import string

def generate_password():
    while True:
        length = int(input("Enter desired password length (minimum 8): "))
        if length < 8:
            print("Password must be at least 8 characters long.")
            continue

        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        if not (use_upper or use_lower or use_numbers or use_special):
            print("You must select at least one character type.")
            continue

        chars = ""
        if use_upper:
            chars += string.ascii_uppercase
        if use_lower:
            chars += string.ascii_lowercase
        if use_numbers:
            chars += string.digits
        if use_special:
            chars += "!@#$%^&*()_+-=[]{}|;:',.<>?/"

        password = []
        if use_upper:
            password.append(random.choice(string.ascii_uppercase))
        if use_lower:
            password.append(random.choice(string.ascii_lowercase))
        if use_numbers:
            password.append(random.choice(string.digits))
        if use_special:
            password.append(random.choice("!@#$%^&*()_+-=[]{}|;:',.<>?/"))

        while len(password) < length:
            password.append(random.choice(chars))

        random.shuffle(password)

        final_password = ''.join(password)
        print("\nGenerated Password:", final_password)

        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            print("See Ya!")
            break

generate_password()