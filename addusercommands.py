import subprocess
import shlex

bash_shell = '/bin/bash'
cshell = '/bin/csh'
user_arr = []


def get_usrs(usr_group):
    with open('{}files/{}cleartextpass.txt'.format(usr_group, usr_group), 'r') as user_list:
        for user in user_list:
            user = user.strip('\n')
            splited = user.split(':')
            user_arr.append(splited)


def get_usr_id():

    userid_args = shlex.split("awk -F ':' '/home/ {print $3}' /etc/passwd")
    userid_get = subprocess.Popen(userid_args, stdout=subprocess.PIPE)
    userid_output = userid_get.communicate()
    userid_output = userid_output[0].decode('utf-8')
    userid_output = userid_output.split('\n')
    last_userid = userid_output[-2]

    return last_userid


def define_password(define_password_username, define_password_pass):
    echo_command_args = shlex.split("echo -e '{}\n{}\n'".format(define_password_pass, define_password_pass))
    password_command_args = shlex.split('passwd {}'.format(define_password_username))

    echo_command = subprocess.Popen(echo_command_args, stdout=subprocess.PIPE)
    password_command = subprocess.Popen(password_command_args, stdin=echo_command.stdout, stdout=subprocess.PIPE)
    echo_command.stdout.close()
    password_command.communicate()


def admin_add(groupname):
    admin_skel = '/etc/skel/adminskel'
    get_usrs(groupname)
    userid = int(get_usr_id()) + 1

    for combo in range(len(user_arr)):
        password = user_arr[combo][1]
        username = user_arr[combo][0]

        adduser_command_args = shlex.split('useradd -m -d /home/admin/users/{} -u {} -G {} -k {} -s {} {}'.format(username, userid, groupname, admin_skel, bash_shell, username))
        subprocess.call(adduser_command_args)

        define_password(username, password)

        userid += 1


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


def developer_add(groupname):
    developer_skel = '/etc/skel/developerskel'
    get_usrs(groupname)
    userid = int(get_usr_id()) + 1

    for combo in range(len(user_arr)):
        password = user_arr[combo][1]
        username = user_arr[combo][1]

        adduser_command_args = shlex.split('useradd -m -d /home/developer/users/{} -u {} -s {} -G {} -k {} {}'.format(username, userid, cshell, groupname, developer_skel, username))
        subprocess.call(adduser_command_args)

        define_password(username, password)
        userid += 1


def temp_add(groupname):
    temp_skel = '/etc/skel/tempskel'
    get_usrs(groupname)
    userid = int(get_usr_id()) + 1

    for combo in range(len(user_arr)):
        password = user_arr[combo][1]
        username = user_arr[combo][1]
        date_command_args = shlex.split('date --date="60 days" +%Y-%m-%d')
        date_command = subprocess.Popen(date_command_args, stdout=subprocess.PIPE)
        date_60_days = date_command.communicate()[0]

        adduser_command_args = shlex.split('useradd -m -d /home/temp/users/{} -u {} -G {} -k {} -s {} -e {} {}'.format(username, userid, groupname, temp_skel, bash_shell, date_60_days, username))
        subprocess.call(adduser_command_args)

        date_command.stdout.close()

        define_password(username, password)
        userid += 1

