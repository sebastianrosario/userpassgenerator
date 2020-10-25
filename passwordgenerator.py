import random
import string
import hashlib


def string_encode(s):
    return s.encode('utf-8', 'replace')


def password_generator():
    validated_letters = list(string.ascii_lowercase)
    temp_pass = []
    for i in range(0, 10):
        i = random.randrange(26)
        temp_pass.append(validated_letters[i])

    final_pass = ''.join(temp_pass) + str(random.randint(1, 1500))
    hashed_pass = hash_password(string_encode(final_pass))
    return final_pass, hashed_pass


def hash_password(passwd):
    h = hashlib.sha256()
    h.update(passwd)
    return h.hexdigest()


def write_password_to_file(group):
    cleartext = open('{}files/{}cleartextpass.txt'.format(group, group), 'a')
    hashed = open('{}files/{}hashedpass.txt'.format(group, group), 'a')
    with open('{}files/{}usernames.txt'.format(group, group), 'r') as file:
        for username in file:
            username.strip()
            current_pass = password_generator()
            hashed_pass = current_pass[1]
            cleartext.write(username.strip('\n') + ':' + current_pass[0] + '\n')
            hashed.write(username.strip('\n') + ':' + hashed_pass + '\n')

    cleartext.close()
    hashed.close()


