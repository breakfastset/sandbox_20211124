"""
Check Login Credentials.

Password Checker. Created by Owen Grady. 24-11-2021
"""


def main():
    """Start Program."""
    password = "12345678"
    if check_password(password):
        print("Logged in")
    else:
        print("Illegal access")


def check_password(password):
    return password == "12345678"


main()
