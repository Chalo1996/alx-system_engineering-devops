#Shell Permissions#
**Commands and Their Functions**
1. sudo su betty- switches the current user to the user betty.
2. whoami- prints the effective username of the current user.
3. groups- prints all the groups the current user is part of.
4. sudo chown betty hello- changes the owner of the file hello to the user betty.
5. touch hello- creates an empty file called hello.
6. sudo chmod +100 hello- adds execute permission to the owner of the file hello.
7. sudo chmod +114 hello- adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
8. sudo chmod +111 hello- adds execution permission to the owner, the group owner and the other users, to the file hello.
9. sudo chmod 007 hello- sets the permission to the file hello as follows:

    Owner: no permission at all
    Group: no permission at all
    Other users: all the permissions
10. sudo chmod 753 hello- sets the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello.
11. sudo chmod --reference=olleh hello- sets the mode of the file hello the same as olleh’s mode.
12. sudo chmod -R a+X- adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
13. mkdir -m 751 my_dir- creates a directory called my_dir with permissions 751 in the working directory.
14. sudo chgrp school hello- changes the group owner to school for the file hello.
15. sudo chown vincent:staff *- changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.*
16. sudo chown -h vincent:staff _hello- changes the owner and the group owner of _hello to vincent and staff respectively.

    The file _hello is in the working directory
    The file _hello is a symbolic link
17. sudo chown --from=guillaume betty hello- changes the owner of the file hello to betty only if it is owned by the user guillaume.

    The file hello will be in the working directory
18. telnet towel.blinknlights.nl- will play the StarWars IV episode in the terminal.
