import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passwords(num_passwords, length):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    try:
        # Get user input for password length and number of passwords
        password_length = int(input("Enter the length of the passwords: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        # Generate passwords
        passwords = generate_passwords(num_passwords, password_length)

        # Display generated passwords
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"Password {i}: {password}")

    except ValueError:
        # Handle invalid input
        print("Please enter valid numeric values for length and number of passwords.")

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
