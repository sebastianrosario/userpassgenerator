import usernamegenerator
import passwordgenerator
import addusercommands
import sys


class InvalidArguments(Exception):
    """Raises when the user does not input the right ammount of command line arguments"""
    pass


def main():
    print(sys.version)
    if len(sys.argv) == 3:
        print('Generating usernames and writing to processedusernames.txt...')
        usernamegenerator.write_users_to_file(sys.argv[2], sys.argv[1])
        print('Generating passwords...')
        passwordgenerator.write_password_to_file(sys.argv[1])
        if sys.argv[1] == 'admin':
            print('Adding users to specified group...')
            addusercommands.admin_add(sys.argv[1])
        elif sys.argv[1] == 'developer':
            addusercommands.developer_add(sys.argv[1])
        elif sys.argv[1] == 'staff':
            addusercommands.staff_add(sys.argv[1])
        elif sys.argv[1] == 'temp':
            addusercommands.temp_add(sys.argv[1])
    else:
        raise InvalidArguments('Pass which group to add the usernames to and then the username file.\nExample: "python3 main.py staff usernames.txt"')


if __name__ == '__main__':
    main()
