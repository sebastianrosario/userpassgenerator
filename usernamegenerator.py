# Importing dependecies
from os import path
import hashcheck

# Declaring arrays for the processed full name, each coliision, and non collision instances
full_name = []
collision = []
normal = []


# This function takes the argument f which is a file of full names, strips the newline character, puts it in lowercase,
# and appends it to the full name array
def process_file(f):
    for line in f:
        line = line.strip('\n')
        line = line.lower()
        full_name.append(line.split(' '))


# Loops through iterable and checks for non unique items.
def find_collisions(ff):
    # Loops through tuple while keeping track of the index
    for i in range(0, len(ff)):
        # Declares the default username rules, first letter + last name
        # and collision username rules which is the full first name + last name
        normal_username_rules = str(ff[i][0])[0:1] + str(ff[i][-1])
        collision_username_rules = str(ff[i][0]) + str(ff[i][-1])

        # If statement that checks if the counter of the loop is at the end of the array
        if i < len(ff)-1:
            # Checks to see if current index is equal to next index, if true append this index to another array
            # using the predefined collision rules
            if str(ff[i][-1]) == str(ff[i + 1][-1]) and str(ff[i][0])[0:1] == str(ff[i + 1][0])[0:1]:
                collision.append(collision_username_rules)

            # Checks to see if current index is equal to the previous index, if true appends current index
            # to collision array
            elif str(ff[i][-1]) == str(ff[i - 1][-1]) and str(ff[i][0])[0:1] == str(ff[i - 1][0])[0:1]:
                collision.append(collision_username_rules)

            # If the current index is not equal to both the next and last index, append using normal username rules
            else:
                normal.append(normal_username_rules)

        # Checks to see if the current counter of the loop is at the end of the iterable, if so append it with the normal
        # username rules. If there was a collision the if statement above would have caught it.
        elif i == len(ff)-1:
            normal.append(str(ff[i][0])[0:1] + str(ff[i][-1]))
        else:
            print('File Empty!')


# Function that takes collision and normal array and compares each value in them to the usernames in processedusernames.txt
# This checks for collisions in the system rather than coliisions in the input file
# Takes two arguments, input file and the group that the final usernames are going to be added to
def write_users_to_file(input_file, output_group):
    # Opens input file to be used
    with open(input_file, 'r') as username_file:
        # Opens the respective groups folder and makes or appends a [GROUP]usernames.txt file
        output_group_file = open('{}files/{}usernames.txt'.format(output_group, output_group), 'a')

        # Processes input file first
        process_file(username_file)

        # Changes the full_name array to a tuple
        tuple_names = tuple(full_name)

        # Sorts the names in alphabetical order by last name
        tuple_names = sorted(tuple_names, key=lambda name: name[-1])

        # Calls find_collisions with find collisions inside the tuple itself
        find_collisions(tuple_names)

        # This next block of code finds if there are any collisions with usernames already in the system and prompts user
        # to select a new username for that specific collision
        if path.exists('processedusernames.txt'):
            with open('processedusernames.txt', 'a') as processed_users:

                # Keeps a counter of the collision array, iterates through each index.
                for collision_counter in range(len(collision)):

                    # Makes sure that the validate_usernames function return False before writing username in collision array to
                    # processedusers.txt and their group's folder
                    if not hashcheck.validate_usernames(collision[collision_counter], 'processedusernames.txt'):
                        print(collision[collision_counter])
                        processed_users.write(collision[collision_counter] + '\n')
                        output_group_file.write(collision[collision_counter] + '\n')

                    # If a collision with the system usernames are detected then the user is prompted to type in a new
                    # username for that instance
                    else:
                        collision[collision_counter] = str(input('\nCollision Was detected for {} Please select a different username. \n'.format(collision[collision_counter])))
                        print(collision[collision_counter])
                        processed_users.write(collision[collision_counter] + '\n')
                        output_group_file.write(collision[collision_counter] + '\n')

                # Keeps a counter while iterating through the normal username rules array
                for normal_counter in range(len(normal)):

                    # Checks to make sure the any username in the normal array does not collide with system usernames before
                    # writing to processedusers.txt and group's folder
                    if not hashcheck.validate_usernames(normal[normal_counter], 'processedusernames.txt'):
                        print(normal[normal_counter])
                        processed_users.write(normal[normal_counter] + '\n')
                        output_group_file.write(normal[normal_counter] + '\n')

                    # Prompts user to input another username for any collisions found
                    else:
                        normal[normal_counter] = str(input('\nCollision was detected for {}. Please select a different username. \n'.format(normal[normal_counter])))
                        print(normal[normal_counter])
                        processed_users.write(normal[normal_counter] + '\n')
                        output_group_file.write(normal[normal_counter] + '\n')

        # Prompts user to make processedusers.txt if it is not present.
        else:
            print('Please create a file named processedusers.txt and add all existing usernames to avoid collisions with created usernames!')

        output_group_file.close()
