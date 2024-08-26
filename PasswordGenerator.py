import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters
    elif complexity == 3:
        characters = string.ascii_letters + string.digits
    elif complexity == 4:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity must be between 1 and 4")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
length = int(input("Enter the desired password length: "))
complexity = int(input("Enter the desired complexity (1-4): "))

password = generate_password(length, complexity)
print(f"Generated password: {password}")
