# Importing all dependencies to generate a random password
import random
import string
import hashlib


# Function that encodes any string passed to it with utf-8
def string_encode(s):
    return s.encode('utf-8', 'replace')


# Uses hashlib to hash input and return the hexidecimal hash
def hash_password(passwd):
    h = hashlib.sha256()
    h.update(passwd)
    return h.hexdigest()


# Function that randomly generates a 11-14 character long password, returns cleartext and hashed password
def password_generator():
    # Storing all posible ascii lowercase letters
    validated_letters = list(string.ascii_lowercase)

    # Making a temporary password array that holds each randomly generated letter
    temp_pass = []

    # Loops 10 times, appending a random letter to temp_pass each time.
    for i in range(0, 10):
        i = random.randrange(26)
        temp_pass.append(validated_letters[i])

    # Joins each letter in the array to a single string, adds a random integer at the end of the password
    final_pass = ''.join(temp_pass) + str(random.randint(1, 1500))
    # Hashes final_pass using encoded string
    hashed_pass = hash_password(string_encode(final_pass))
    return final_pass, hashed_pass


def write_password_to_file(group):
    # Opens or creates neccesary files to store each username/password combination
    cleartext = open('{}files/{}cleartextpass.txt'.format(group, group), 'a')
    hashed = open('{}files/{}hashedpass.txt'.format(group, group), 'a')
    # Opens the groups username file
    with open('{}files/{}usernames.txt'.format(group, group), 'r') as file:
        # Loops through each username (excluding white space), generates a password for it
        # and pairs the two in clear text and hashed form in two different files
        for username in file:
            if username != '\n':
                current_pass = password_generator()
                hashed_pass = current_pass[1]
                cleartext.write(username.strip('\n') + ':' + current_pass[0] + '\n')
                hashed.write(username.strip('\n') + ':' + hashed_pass + '\n')

    cleartext.close()
    hashed.close()


