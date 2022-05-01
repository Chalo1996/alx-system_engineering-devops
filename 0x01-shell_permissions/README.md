**Shell Permissions**</br>

**Commands and Their Functions**</br>

1. sudo su betty- switches the current user to the user betty.</br>
2. whoami- prints the effective username of the current user.</br>
3. groups- prints all the groups the current user is part of.</br>
4. sudo chown betty hello- changes the owner of the file hello to the user betty.</br>
5. touch hello- creates an empty file called hello.</br>
6. sudo chmod +100 hello- adds execute permission to the owner of the file hello.</br>
7. sudo chmod +114 hello- adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.</br>
8. sudo chmod +111 hello- adds execution permission to the owner, the group owner and the other users, to the file hello.</br>
9. sudo chmod 007 hello- sets the permission to the file hello as follows:</br>

    Owner: no permission at all
    Group: no permission at all
    Other users: all the permissions
10. sudo chmod 753 hello- sets the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello.</br>
11. sudo chmod --reference=olleh hello- sets the mode of the file hello the same as olleh’s mode.</br>
12. sudo chmod -R a+X- adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.</br>
13. mkdir -m 751 my_dir- creates a directory called my_dir with permissions 751 in the working directory.</br>
14. sudo chgrp school hello- changes the group owner to school for the file hello.</br>
15. sudo chown vincent:staff *- changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.*</br>
16. sudo chown -h vincent:staff _hello- changes the owner and the group owner of _hello to vincent and staff respectively.</br>

    The file _hello is in the working directory
    The file _hello is a symbolic link
17. sudo chown --from=guillaume betty hello- changes the owner of the file hello to betty only if it is owned by the user guillaume.</br>

    The file hello will be in the working directory
18. telnet towel.blinknlights.nl- will play the StarWars IV episode in the terminal.</br>
