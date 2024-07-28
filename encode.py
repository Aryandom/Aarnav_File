def encode(password):
    encoded_password = ''
    for char in password:
        encoded_password += str((int(char) + 3) % 10)
    return encoded_password

