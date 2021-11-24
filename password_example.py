"""
Check Login Credentials.

Password Checker. Created by Owen Grady. 24-11-2021
"""


def main():
    """Start Program."""
    password = input("Enter a password")

    if check_password(password):
        print("Logged in")
    else:
        print("Illegal access")


def check_password(password):
    """Check if password is valid"""
    return password == "12345678"


main()
