def decode(password):
    pw = ''
    for char in password:
        pw += str((int(char) - 3) % 10)
    return pw
