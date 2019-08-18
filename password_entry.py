"""Zachary Keeffe"""
PASSWORD_LENGTH_MINIMUM = 4


def main():
    password = ""
    while len(password) < PASSWORD_LENGTH_MINIMUM:
        password = input("Please enter a password: ")
        if len(password) < PASSWORD_LENGTH_MINIMUM:
            print("Insufficient Password Length.")
    print("Entry: ", "*" * len(password))


main()
