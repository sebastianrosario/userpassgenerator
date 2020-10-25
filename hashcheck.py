import hashlib


def string_encode(s):
    return s.encode('utf-8', 'replace')


def validate_usernames(current_username, file):
    current_username = string_encode(current_username)
    with open(file, 'r') as processed_username_file:
        proc = []
        for usernames in processed_username_file:
            proc.append(usernames.strip('\n'))

        for processed_usernames in proc:
            h = hashlib.sha256()
            processed_usernames = string_encode(processed_usernames)
            h.update(processed_usernames)

            m = hashlib.sha256()
            m.update(current_username)

            if m.hexdigest() == h.hexdigest():
                return True
            else:
                return False



