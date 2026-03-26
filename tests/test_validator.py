from validator import Validator 

def test_valid_name():
    assert Validator.validate_name("Ayush")


def test_invalid_name():
    assert not Validator.validate_name("Ay")


def test_valid_email():
    assert Validator.validate_email("Ayush.singh@bridgelabz.com")

def test_invalid_email():
    assert not Validator.validate_email("abac@gmai.com")

def test_valid_phone():
    assert  Validator.validate_phone("91 9026960970")

def test_invalid_phone():
    assert not Validator.validate_phone("9026960970")