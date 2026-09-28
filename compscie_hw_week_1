password = None

def password_creation():
    global password
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    requirements = "Password must have 5-10 characters, at least 1 special character, and at least 1 number."
    print("-" * len(requirements))
    print(requirements)
    print("-" * len(requirements))
    password = input("Enter your password here: ")

    if string_length_between(password, 5, 10):
        if string_contains_numbers(password):
            if string_contains_special(password):
                print("Password accepted")
                print(password)
                confirm()
            else:
                print("Error: Password had no special characters")
                password_creation()
        else:
            print("Error: Password has no numbers")
            password_creation()
    else:
        print("Error: Invalid password length")
        password_creation()

def string_length_between(theString, min, max):
    return len(theString) >= min and len(theString) <= max

def string_contains_numbers(theString):
    for character in theString:
        if character.isnumeric():
            return True
    return False

def string_contains_special(theString):
    special_characters = list("@!§$%&/()=?")
    for character in theString:
        if character in special_characters:
            return True
    return False

def confirm():
    confirmation = input("Re-enter your password: ")
    if confirmation == password:
        print("You have confirmed your password.")
    else:
        print("-" * len("Incorrect"))
        print("Incorrect")
        print("-" * len("Incorrect"))
        password_creation()

if __name__ == "__main__":
    password_creation()
