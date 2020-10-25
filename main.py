# Importing all dependencies including other Python files used to created usernames, passwords,
# and using useradd to add them to the server
import usernamegenerator
import passwordgenerator
import addusercommands
import sys


class InvalidArguments(Exception):
    """Raises when the user does not input the right ammount of command line arguments"""
    pass


def main():
    # Prints the version of Python that the user runs the script on.
    print(sys.version)

    # If statment checks if the user passed the script that right amount of command line agruments.
    # Correct syntax: python3 main.py [GROUP] [USERNAMEFILE]
    if len(sys.argv) == 3:
        # Calling the usernamegenerator.py function that uses the input file to create usernames and save it to
        # processedusernames.txt and their own groups folder
        print('Generating usernames and writing to processedusernames.txt...')
        usernamegenerator.write_users_to_file(sys.argv[2], sys.argv[1])

        # Calling the passwordgenerator.py function that generates passwords for each username in
        # [GROUP]files/[GROUP]usernames.txt and then outputs those username/password combos to  their respective password files
        print('Generating passwords...')
        passwordgenerator.write_password_to_file(sys.argv[1])

        # If statement checks which group the usernames/password combinations are going to be added in, calls the correct
        # addusercommands.py function that will add those usernames to the correct group with different options
        if sys.argv[1] == 'admin':
            print('Adding users to specified group...')
            addusercommands.admin_add(sys.argv[1])
        elif sys.argv[1] == 'developer':
            addusercommands.developer_add(sys.argv[1])
        elif sys.argv[1] == 'companystaff':
            addusercommands.staff_add(sys.argv[1])
        elif sys.argv[1] == 'temp':
            addusercommands.temp_add(sys.argv[1])
    else:
        # Raises Exception defined earlier if the user does not pass enough arguments or too many.
        raise InvalidArguments('Pass which group to add the usernames to and then the username file.\nExample: "python3 main.py staff usernames.txt"')


if __name__ == '__main__':
    main()
