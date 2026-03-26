from user import User
from validator import Validator
from utils import get_input


def main():
    first_name = get_input("First Name" , Validator.validate_name , "Invalid first name")
    last_name = get_input("Last Name" , Validator.validate_name , "Invalid Last name")
    email = get_input("Email" , Validator.validate_email , "INvalid Email")
    phone = get_input("Phone" , Validator.validate_phone , "Invalid Phone")
    password = get_input("Password", Validator.validate_password,"Password must have atleast 8 characters")

    user = User(first_name , last_name  , email , phone)

    print("\n User Registered Successfully")
    print(user)


if __name__ == "__main__":
    main()