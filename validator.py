import re

class Validator:
    NAME_PATTERN = r"^[A-Z][a-z]{3,}$"
    EMAIL_PATTERN = r"^[\w]+(\.[\w]+)@[a-zA-Z]+\.[\w]"
    PHONE_PATTERN = r'^[0-9]{2}\s[0-9]{10}$'
    PASSWORD_PATTERN = r'^(?=.*[A-Z])(?=.*[0-9])(?=[^!@#$%^&*]*[!@#$%^&*][^!@#$%^&*]*$).{8,}$'

    
    @staticmethod
    def validate_password(password):
        return bool(re.fullmatch(Validator.PASSWORD_PATTERN , password))

    @staticmethod
    def validate_name(name):
        return bool(re.match(Validator.NAME_PATTERN ,name))
    
    @staticmethod
    def validate_email(email):
        return bool(re.match(Validator.EMAIL_PATTERN,email))
    
    @staticmethod
    def validate_phone(phone):
        return bool(re.match(Validator.PHONE_PATTERN, phone))