# Importing the hash library used by Python
import hashlib


# Defining function that encodes any string passed to it in utf-8
def string_encode(s):
    return s.encode('utf-8', 'replace')


# Function that validates a username passed to it against a username in a file
def validate_usernames(current_username, file):

    # Enconding the current username for use in hashing later
    current_username = string_encode(current_username)

    # Opens input file
    with open(file, 'r') as processed_username_file:
        # Array that holds each username in the input file after looping through each line of that file
        proc = []
        for usernames in processed_username_file:
            proc.append(usernames.strip('\n'))

        # Encodes each username in input file, encodes the current username and compares the two
        # Returns True or false depending on the result
        for processed_usernames in proc:

            # Declaring a hash object
            h = hashlib.sha256()

            # Encoding the username from the input file
            processed_usernames = string_encode(processed_usernames)

            # Updating the hash object with the value of the processed username
            h.update(processed_usernames)

            # Declaring hash object for the current username
            m = hashlib.sha256()

            # Updating the hash object with the value of the current username
            m.update(current_username)

            # Comparing each processed username with the current username
            if m.hexdigest() == h.hexdigest():
                return True
            else:
                return False
