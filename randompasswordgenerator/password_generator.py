
import secrets
import string


def generate_password(length):
    """Generate a secure password containing all four character types."""

    if length < 8 or length > 128:
        raise ValueError("Password length must be between 8 and 128.")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+?"

    # Select at least one character from each category.
    password_chars = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    # Combine all allowed characters.
    all_chars = uppercase + lowercase + digits + symbols

    # Fill the remaining positions.
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_chars))

    # Shuffle securely so required characters aren't predictable.
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("=" * 42)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 42)
    print("Choose a password length between 8 and 128.")
    print("Your password will contain uppercase letters,")
    print("lowercase letters, numbers, and symbols.")

    while True:
        try:
            length = int(input("\nEnter password length: "))
            password = generate_password(length)

            print("\nYour generated password is:")
            print(password)
            print(f"Password length: {len(password)}")

        except ValueError as error:
            print(f"\nInvalid input: {error}")

        again = input(
            "\nGenerate another password? (yes/no): "
        ).strip().lower()

        if again not in ("yes", "y"):
            print("\nThank you for using the generator!")
            break


if __name__ == "__main__":
    main()