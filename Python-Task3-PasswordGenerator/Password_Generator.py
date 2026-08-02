import random
import string


def get_length():
    while True:
        length = input("Enter desired password length (minimum 8): ")
        try:
            length = int(length)
            if length < 8:
                print("Password length must be at least 8. Please try again.")
                continue
            return length
        except ValueError:
            print("That's not a valid number. Please try again.")


def get_character_choices():
    while True:
        print("\nChoose which character types to include (answer y/n for each):")
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
        use_digits = input("Include numbers? (y/n): ").strip().lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

        chosen_count = sum([use_upper, use_lower, use_digits, use_symbols])

        if chosen_count < 2:
            print("Please select at least 2 character types. Try again.\n")
            continue

        return use_upper, use_lower, use_digits, use_symbols


def build_character_pool(use_upper, use_lower, use_digits, use_symbols):
    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool


def generate_password(length, pool):
    password = ""
    for i in range(length):
        password += random.choice(pool)
    return password


def main():
    print("=== Random Password Generator ===")

    while True:
        length = get_length()
        use_upper, use_lower, use_digits, use_symbols = get_character_choices()
        pool = build_character_pool(use_upper, use_lower, use_digits, use_symbols)

        password = generate_password(length, pool)
        print(f"\nGenerated password: {password}")

        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
