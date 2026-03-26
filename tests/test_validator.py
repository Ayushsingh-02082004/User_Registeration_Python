from validator import Validator 

def test_valid_name():
    assert Validator.validate_name("Ayush")


def test_invalid_name():
    assert not Validator.validate_name("Ay")


# def test_valid_email():
#     assert Validator.validate_email("Ayush.singh@bridgelabz.com")


def test_valid_emails_uc9():
    valid_emails = [
        "abc@yahoo.com",
        "abc-100@yahoo.com",
        "abc.100@yahoo.com",
        "abc111@abc.com",
        "abc-100@abc.net",
        "abc.100@abc.com.au",
        "abc@1.com",
        "abc@gmail.com.com",
        "abc+100@gmail.com",
        "Ayush.singh@bridgelabz.com"
    ]

    for email in valid_emails:
        assert Validator.validate_email(email), f"Failed for: {email}"

# def test_invalid_email():
#     assert not Validator.validate_email("abac@.com")

def test_invalid_emails_uc9():
    invalid_emails = [
        "abc",
        "abc@.com.my",
        "abc123@gmail.a",
        "abc123@.com",
        "abc123@.com.com",
        ".abc@abc.com",
        "abc()*@gmail.com",
        "abc@%*.com",
        "abc..2002@gmail.com",
        "abc.@gmail.com",
        "abc@abc@gmail.com",
        "abc@gmail.com.1a",
        "abc@gmail.com.aa.au"
    ]

    for email in invalid_emails:
        assert not Validator.validate_email(email), f"Failed for: {email}"

def test_valid_phone():
    assert  Validator.validate_phone("91 9026960970")

def test_invalid_phone():
    assert not Validator.validate_phone("9026960970")