import subprocess
import shlex

bash_shell = '/bin/bash'
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


def admin_add(groupname):
    admin_skel = '/etc/skel/adminskel'
    get_usrs(groupname)
    userid = int(get_usr_id()) + 1

    for combo in range(len(user_arr)):
        password = user_arr[combo][1]
        adduser_command_args = shlex.split('useradd -m -d /home/admin/users/{} -u {} -G {} -k {} -s {} {}'.format(user_arr[combo][0], userid, groupname, admin_skel, bash_shell, user_arr[combo][0]))
        echo_command_args = shlex.split("echo -e '{}\n{}\n'".format(password, password))
        password_command_args = shlex.split('passwd {}'.format(user_arr[combo][0]))

        subprocess.call(adduser_command_args)
        echo_command = subprocess.Popen(echo_command_args, stdout=subprocess.PIPE)
        password_command = subprocess.Popen(password_command_args, stdin=echo_command.stdout, stdout=subprocess.PIPE)
        echo_command.stdout.close()
        password_command.communicate()
        userid += 1


def staff_add(groupname):
    staff_skel = '/etc/skel/staffskel'
    get_usrs(groupname)
    userid = int(get_usr_id()) + 1

    for combo in range(len(user_arr)):
        adduser_command_args = shlex.split('useradd -m -d /home/staff/users/{} -u {} -G {} -k {} -s {} {}'.format(user_arr[combo][0], userid, groupname, staff_skel, bash_shell, user_arr[combo][0]))
        subprocess.call(adduser_command_args)
        userid += 1


def developer_add(groupname):
    developer_skel = '/etc/skel/developerskel'
    cshell = '/bin/csh'
    get_usrs(groupname)
    userid = int(get_usr_id()) + 1
    for combo in range(len(user_arr)):
        adduser_command_args = shlex.split('useradd -m -d /home/developer/users/{} -u {} -s {} -G {} -k {} {}'.format(user_arr[combo][0], userid, cshell, groupname, developer_skel, user_arr[combo][0]))
        subprocess.call(adduser_command_args)
        print(adduser_command_args)
        userid += 1


def temp_add(groupname):
    temp_skel = '/etc/skel/tempskel'
    get_usrs(groupname)
    userid = int(get_usr_id()) + 1

    for combo in range(len(user_arr)):
        adduser_command_args = shlex.split('useradd -m -u {} -G {} -k {} -s {} {}'.format(userid, groupname, temp_skel, bash_shell, user_arr[combo][0]))
        subprocess.call(adduser_command_args)
        print(adduser_command_args)
        userid += 1

