import random
import string

def generate_password(length):
    if length < 4:
        return " Password length must be at least 4 characters."

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensures at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password with random choices
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)  # Shuffle to avoid predictable pattern
    return ''.join(password)

def main():
    print(" Random Password Generator")
    try:
        length = int(input("Enter desired password length (min 4): "))
        password = generate_password(length)
        print("\n Generated Password:", password)
    except ValueError:
        print(" Please enter a valid number.")

if __name__ == "__main__":
    main()
