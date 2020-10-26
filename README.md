# userpassgenerator
Userpassgenerator is a Python script takes an input file with full name returns a [USERNAME]:[PASSWORD] combination and then adds those usernames to a Linux server in a specific group. The user add is handled by shell commands through Python. 

Syntax:

``` python3 main.py [GROUP] [NAME_LIST] ```

## Assumptions
Userpassgenerator assumes that the directory structure for each group is:

> ```  /home/[GROUP]/users/[USERNAME] ```

The skeleton directory structure is as follows:

>  ``` /etc/skel/[GROUP]skel ```

These two things are things that userpassgenerator does not create so they have to exist beforehand.

Existing usernames have to added to the <i>processedusernames.txt</i> to avoid username collisions with existing usernames. 
Username collisions within the input file are handled by the script.

## Username Rules
Normal Username Rules:
> ``` [firstletter][lastname] ```

> ``` e.g Alice Wu ---> awu ```

Collision Username Rules:
> ``` [firstname][lastname] ```
> ``` e.g Alice Wu ---> alicewu ```

Each username rule chooses the final last name in the string. Hyphens are not removed.

## Requisites 

> Python 3.x.x

> Groups: admin, developer, companystaff, temp

> A name list with the format [FIRSTNAME] [LASTNAME] (Does not matter if there are multiple last names).
