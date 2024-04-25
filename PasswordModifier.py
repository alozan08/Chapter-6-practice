'''
    Many user-created passwords are simple and easy to guess.
    Write a program that takes a simple password and makes it
    stronger by replacing characters using the key below, and by
    appending "!" to the end of the input string.
    i becomes 1
    a becomes @
    m becomes M
    B becomes 8
    s becomes $
    example input: mypassword
        output: Myp@$$word!

'''

def passModifier(password):
    newPassword = ""
    for letter in password:
        if letter == 'i':
            newPassword += '1'
        elif letter == 'a':
            newPassword += '@'
        elif letter == 'm':
            newPassword += 'M'
        elif letter == 'B':
            newPassword += '8'
        elif letter == 's':
            newPassword += '$'
        else:
            newPassword += letter
    newPassword += '!'
    return newPassword

insecure_pass = 'mypassword'
print(passModifier(insecure_pass))