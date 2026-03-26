import re


class User:
    def __init__(self, firstname , lastname):
        self.firstname = firstname
        self.lastname = lastname


    def __str__(self):
        return f"First Name: {self.firstname} LastName: {self.lastname}"
    
    

class Validator:
    @staticmethod
    def validate_first_name(name):
        pattern = r'^[A-Z][a-z]{2,}$'
        return re.match(pattern, name)
    
    @staticmethod
    def validate_last_name(name):
        pattern = r"^[A-Z][a-z]{3,}$"
        return re.match(pattern ,name)
    
    @staticmethod
    def validate_email(email):
        pattern = r"^[\w]+(\.[\w]+)@[\w]+\.[\w]"
        return re.match(pattern , email)
    


def get_input(field, validation_func, error_message):
    while True:
        value = input(f"Enter {field}: ")
        if validation_func(value):
            return value
        else:
            print(f"Error: {error_message}")


def main():
    firstname = get_input(
        "First Name",
        Validator.validate_first_name,
        "First Name should start with a capital letter and have at least 3 characters"
    )

    lastname = get_input(
        "Last Name",
        Validator.validate_last_name,
        "Last name should start with a capital letter and should have at least 3 characters"
    )

    email = get_input("Email" ,Validator.validate_email,"Enter like ayush.singh@bridgelabz.com");

    user = User(firstname , lastname)
    print("\nUser Registered Successfully!")
    print(user)
    print(f"Email : {email}")


if __name__ == "__main__":
    main()