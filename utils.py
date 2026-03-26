def get_input(field , validatorFunc , errormessage):
    while True:
        value = input(f"Enter {field}: ")
        if validatorFunc(value):
            return value
        print(f"Error: {errormessage}")