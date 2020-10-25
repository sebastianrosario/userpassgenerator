import subprocess
import shlex

# Declaring useful variables for each function, regardless of group
bash_shell = '/bin/bash'
cshell = '/bin/csh'
user_arr = []


# Opens the group cleartext password file and splits each pair into a [username, password] array
def get_usrs(usr_group):
    with open('{}files/{}cleartextpass.txt'.format(usr_group, usr_group), 'r') as user_list:
        for user in user_list:
            user = user.strip('\n')
            splited = user.split(':')
            user_arr.append(splited)


# Uses awk to return the last userid that was used in the system
def get_usr_id():

    # Storing the shell command that was split into its parts
    userid_args = shlex.split("awk -F ':' '/home/ {print $3}' /etc/passwd")

    # Starting the process of awk
    userid_get = subprocess.Popen(userid_args, stdout=subprocess.PIPE)

    # Storing that output of awk into userid_output
    userid_output = userid_get.communicate()

    # Decoding the encoded output using utf-8
    userid_output = userid_output[0].decode('utf-8')

    # Spliting that output by new line, useful if there are more than 1 users already created
    userid_output = userid_output.split('\n')

    # Returning the last userid from the array
    last_userid = userid_output[-2]

    return last_userid


# Uses subprocces to define a password for a given username and password
def define_password(define_password_username, define_password_pass):
    # Storing the commands that are going to be using in split form
    echo_command_args = shlex.split("echo -e '{}\n{}\n'".format(define_password_pass, define_password_pass))
    password_command_args = shlex.split('passwd {}'.format(define_password_username))

    # Opening the echo command process and directing its output to pipe
    echo_command = subprocess.Popen(echo_command_args, stdout=subprocess.PIPE)

    # Starting the passwd command process and using the output from echo command as the input for this command
    password_command = subprocess.Popen(password_command_args, stdin=echo_command.stdout, stdout=subprocess.PIPE)

    # Makes sure the echo command runs first
    echo_command.stdout.close()

    # Runs passwd command
    password_command.communicate()


# Uses different useradd options to achieve desired admin group rights
def admin_add(groupname):
    # Declaring the admin skeleton directory
    admin_skel = '/etc/skel/adminskel'

    # Gets the usernames from the group's folder
    get_usrs(groupname)

    # Declares userid variable by calling the get_usr_id function and adding one to the integer result
    userid = int(get_usr_id()) + 1

    # Loops through each user and calls linux commands to add user to server and set their password
    for combo in range(len(user_arr)):
        # Defining each username and password in the array
        password = user_arr[combo][1]
        username = user_arr[combo][0]

        # Calls the useradd command with specialized options that suit the admin group
        adduser_command_args = shlex.split('useradd -m -d /home/admin/users/{} -u {} -G {} -k {} -s {} {}'.format(username, userid, groupname, admin_skel, bash_shell, username))
        subprocess.call(adduser_command_args)

        # Calls earlier function that utilizes linux commands to update the added user's password
        define_password(username, password)

        # Increases the userid for the next user
        userid += 1


# This is much of the same from admin_add but the useradd command has different options that better suit staff group
def staff_add(groupname):
    staff_skel = '/etc/skel/staffskel'
    get_usrs(groupname)
    userid = int(get_usr_id()) + 1

    for combo in range(len(user_arr)):
        password = user_arr[combo][1]
        username = user_arr[combo][0]

        adduser_command_args = shlex.split('useradd -m -d /home/staff/users/{} -u {} -G {} -k {} -s {} {}'.format(username, userid, groupname, staff_skel, bash_shell, username))
        subprocess.call(adduser_command_args)

        define_password(username, password)
        userid += 1


# The same as staff_add but the shell variable is changed to c shell rather than bash
def developer_add(groupname):
    developer_skel = '/etc/skel/developerskel'
    get_usrs(groupname)
    userid = int(get_usr_id()) + 1

    for combo in range(len(user_arr)):
        password = user_arr[combo][1]
        username = user_arr[combo][0]

        adduser_command_args = shlex.split('useradd -m -d /home/developer/users/{} -u {} -s {} -G {} -k {} {}'.format(username, userid, cshell, groupname, developer_skel, username))
        subprocess.call(adduser_command_args)

        define_password(username, password)
        userid += 1


# Adds temp employees to the server the same as the other ones but sets the expiration date to these users 60 days from the time of starting the program
def temp_add(groupname):
    temp_skel = '/etc/skel/tempskel'
    get_usrs(groupname)
    userid = int(get_usr_id()) + 1

    for combo in range(len(user_arr)):
        password = user_arr[combo][1]
        username = user_arr[combo][0]

        # Opens the date command process with options to make it display the date 60 days from the date when the script is run
        # Stores date in format that useradd command can use
        date_command_args = shlex.split('date --date="60 days" +%Y-%m-%d')
        date_command = subprocess.Popen(date_command_args, stdout=subprocess.PIPE)
        date_60_days = date_command.communicate()[0]

        adduser_command_args = shlex.split('useradd -m -d /home/temp/users/{} -u {} -G {} -k {} -s {} -e {} {}'.format(username, userid, groupname, temp_skel, bash_shell, date_60_days, username))
        subprocess.call(adduser_command_args)

        date_command.stdout.close()

        define_password(username, password)
        userid += 1

