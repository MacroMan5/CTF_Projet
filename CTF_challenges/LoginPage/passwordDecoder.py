def get_password():
    # The resultant values after each character of the password is added to 0xCAFE
    resultant_values = [52040, 52018, 52084, 52018, 52049, 52065, 52080, 52015, 52078, 52082]

    password = ""
    for val in resultant_values:
        # Subtract 0xCAFE from each value to get the ASCII code of the character
        ascii_code = val - 0xCAFE

        # Check if the ASCII code is within the valid range
        if 0 <= ascii_code <= 127:
            # Convert the ASCII code to the character and add it to the password string
            password += chr(ascii_code)
        else:
            # Handle the case when the ASCII code is not within the valid range
            password += "?"

    return password

print(get_password())
