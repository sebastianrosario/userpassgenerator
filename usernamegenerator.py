import sys
from os import path
import hashcheck

full_name = []
collision = []
normal = []


def process_file(f):
    for line in f:
        line = line.strip('\n')
        line = line.lower()
        full_name.append(line.split(' '))


def find_collisions(ff):

    for i in range(0, len(ff)):
        normal_username_rules = str(ff[i][0])[0:1] + str(ff[i][-1])
        collision_username_rules = str(ff[i][0]) + str(ff[i][-1])

        if i < len(ff)-1:
            if str(ff[i][-1]) == str(ff[i + 1][-1]) and str(ff[i][0])[0:1] == str(ff[i + 1][0])[0:1]:
                collision.append(collision_username_rules)

            elif str(ff[i][-1]) == str(ff[i - 1][-1]) and str(ff[i][0])[0:1] == str(ff[i - 1][0])[0:1]:
                collision.append(collision_username_rules)

            else:
                normal.append(normal_username_rules)

        elif i == len(ff)-1:
            normal.append(str(ff[i][0])[0:1] + str(ff[i][-1]))
        else:
            print('File Empty!')


def write_users_to_file(input_file, output_group):
    with open(input_file, 'r') as username_file:
        output_group_file = open('{}files/{}usernames.txt'.format(output_group, output_group), 'a')
        process_file(username_file)
        tuple_names = tuple(full_name)
        tuple_names = sorted(tuple_names, key=lambda name: name[-1])
        find_collisions(tuple_names)

        if path.exists('processedusernames.txt'):
            with open('processedusernames.txt', 'a') as processed_users:

                for collision_counter in range(len(collision)):
                    if not hashcheck.validate_usernames(collision[collision_counter], 'processedusernames.txt'):
                        print(collision[collision_counter])
                        processed_users.write(collision[collision_counter] + '\n')
                        output_group_file.write(collision[collision_counter] + '\n')
                    else:
                        collision[collision_counter] = str(input('\nCollision Was detected for {} Please select a different username. \n'.format(collision[collision_counter])))
                        print(collision[collision_counter])
                        processed_users.write(collision[collision_counter] + '\n')
                        output_group_file.write(collision[collision_counter] + '\n')

                for normal_counter in range(len(normal)):
                    if not hashcheck.validate_usernames(normal[normal_counter], 'processedusernames.txt'):
                        print(normal[normal_counter])
                        processed_users.write(normal[normal_counter] + '\n')
                        output_group_file.write(normal[normal_counter] + '\n')
                    else:
                        normal[normal_counter] = str(input('\nCollision was detected for {}. Please select a different username. \n'.format(normal[normal_counter])))
                        print(normal[normal_counter])
                        processed_users.write(normal[normal_counter] + '\n')
                        output_group_file.write(normal[normal_counter] + '\n')

        else:
            print('Making processedusernames.txt')
            with open('processedusernames.txt', 'w') as processed_users:
                for collision_names in collision:
                    print(collision_names)
                    processed_users.write(collision_names + '\n')
                    output_group_file.write(collision_names + '\n')

                for normal_names in normal:
                    print(normal_names)
                    processed_users.write(normal_names + '\n')
                    output_group_file.write(normal_names + '\n')

        output_group_file.close()
