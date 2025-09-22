import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    # Define character pools
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine all characters
    all_chars = lower_chars + upper_chars + digits + symbols

    if not all_chars:
        print("❌ Error: No characters selected to generate password.")
        return None

    # Ensure password contains at least one character from each selected set
    password = []
    if use_upper:
        password.append(random.choice(upper_chars))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    # Fill the rest of the password length with random choices
    remaining_length = length - len(password)
    password += random.choices(all_chars, k=remaining_length)

    # Shuffle the password list to randomize character positions
    random.shuffle(password)

    return ''.join(password)

def main():
    print("🔐 Password Generator")
    
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            if length < 4:
                print("⚠️ Password length should be at least 4.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    use_upper = input("Include uppercase letters? (Y/n): ").strip().lower() != 'n'
    use_digits = input("Include digits? (Y/n): ").strip().lower() != 'n'
    use_symbols = input("Include symbols? (Y/n): ").strip().lower() != 'n'

    password = generate_password(length, use_upper, use_digits, use_symbols)

    if password:
        print("\nGenerated Password:")
        print(password)

if __name__ == "__main__":
    main()
