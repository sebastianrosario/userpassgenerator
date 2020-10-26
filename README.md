# userpassgenerator
Userpassgenerator is a Python script takes an input file with full name returns a [USERNAME]:[PASSWORD] combination and then adds those usernames to a Linux server in a specific group. The user add is handled by shell commands through Python. 

The userid is +1 after the last user with a /home/ directory in the /etc/passwd file

Syntax:

``` python3 main.py [GROUP] [NAME_LIST] ```

## Assumptions
Userpassgenerator assumes that the directory structure for each group is:

> ```  /home/[GROUP]/users/[USERNAME] ```

The skeleton directory structure is as follows:

>  ``` /etc/skel/[GROUP]skel ```

Sudoers file:
> ``` %admin ALL:(ALL) ALL ```

These three things are things that userpassgenerator does not create so they have to exist beforehand.

Existing usernames have to added to the <i>processedusernames.txt</i> to avoid username collisions with existing usernames. 
Username collisions within the input file are handled by the script.

Script will stop if collision is found with the usernames on the system and will ask user for a new username.

## Username Rules
Normal Username Rules:
> ``` [firstletter][lastname] ```

> ``` e.g Alice Wu ---> awu ```

Collision Username Rules:
> ``` [firstname][lastname] ```

> ``` e.g Alice Wu ---> alicewu ```

Each username rule chooses the final last name in the string. Hyphens are not removed.

## Password Rules
Passwords are random strings of 10 lowercase letters and 1-4 integers. These are place holder passwords and are matched to their usernames and stored in clear text. 
Passwords are also hashed and stored in a separate file for verification. 

## Group Options
Admin:
> ``` sudo privleges ```

Developer
> ``` Defaulted to C Shell ```

Temp
> ``` Account expires in 60 days ```

## Requisites 

> Python 3.x.x

> Groups: admin, developer, companystaff, temp

> A name list with the format [FIRSTNAME]...[LASTNAME] (does not matter if there are multiple last names).
