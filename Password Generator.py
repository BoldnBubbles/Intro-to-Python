import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special):
    # Ensure the minimum length is 10 characters
    length = max(10, length)

    # Define character sets based on user preferences
    character_sets = [string.ascii_lowercase]  # Always include lowercase letters
    if include_uppercase:
        character_sets.append(string.ascii_uppercase)
    if include_numbers:
        character_sets.append(string.digits)
    if include_special:
        character_sets.append(string.punctuation)

    # Ensure at least one character from each selected set
    password = [random.choice(char_set) for char_set in character_sets]

    # Fill the rest of the password length with random characters from the selected sets
    all_characters = ''.join(character_sets)
    for _ in range(length - len(password)):
        password.append(random.choice(all_characters))

    # Shuffle the list to make the password unpredictable
    random.shuffle(password)
    
    return ''.join(password)

def main():
    while True:
        length = int(input("How long should the password be? (minimum 10 characters): "))
        if length >= 10:
            break
        print("Password length must be at least 10 characters. Please try again.")

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, include_uppercase, include_numbers, include_special)
    print("Here is your password:", password)

main()
