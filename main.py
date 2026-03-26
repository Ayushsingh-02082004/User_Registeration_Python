import re


class User:
    def __init__(self, firstname):
        self.firstname = firstname


    def __str__(self):
        return f"First Name: {self.firstname}"
    

class Validator:
    @staticmethod
    def validate_first_name(name):
        pattern = r'^[A-Z][a-z]{2,}$'
        return re.match(pattern, name)
    


def get_input(field, validation_func, error_message):
    while True:
        value = input(f"Enter {field}: ")
        if validation_func(value):
            return value
        else:
            print(f"Error: {error_message}")


def main():
    first_name = get_input(
        "First Name",
        Validator.validate_first_name,
        "First Name should start with a capital letter and have at least 3 characters"
    )

    user = User(first_name)
    print("\nUser Registered Successfully!")
    print(user)


if __name__ == "__main__":
    main()