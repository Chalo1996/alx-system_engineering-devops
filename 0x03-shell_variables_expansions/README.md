**Shell, init files, variables and expansions**

<em>
<br>alias ls="rm *" : Create a script that creates an alias.

    Name: ls
    Value: rm *
</br>
<br>echo "hello $USER" : Create a script that prints hello user, where user is the current Linux user.</br>
<br>export PATH="$PATH:/action" : Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.</br>
<br>echo $(($(echo $PATH | grep -o ":/" | wc -l)+1)) : Create a script that counts the number of directories in the PATH.
</br>
<br>printenv : Create a script that lists environment variables.</br>
<br>set : Create a script that lists all local variables and environment variables, and functions.</br>
<br>BEST=School : Create a script that creates a new local variable.

    Name: BEST
    Value: School
</br>
<br>export BEST=School : Create a script that creates a new global variable.

    Name: BEST
    Value: School
</br>
<br>echo $((TRUEKNOWLEDGE+128)) : Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.</br>
<br>echo $((POWER/DIVIDE)) : Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.

    POWER and DIVIDE are environment variables
</br>
<br>echo $((BREATH**LOVE)) : Write a script that displays the result of BREATH to the power LOVE

    BREATH and LOVE are environment variables
    The script should display the result, followed by a new line
</br>
<br>echo $((2#$BINARY)) : Write a script that converts a number from base 2 to base 10.</br>
<br>echo {a..z}{a..z} | tr " " "\n" | grep -v "oo" --max-count=675 : Create a script that prints all possible combinations of two letters, except oo.

    Letters are lower cases, from a to z
    One combination per line
    The output should be alpha ordered, starting with aa
    Do not print oo
    Your script file should contain maximum 64 characters
</br>
<br>printf "%.2f\n" $(echo $NUM) : Write a script that prints a number with two decimal places, followed by a new line.

The number will be stored in the environment variable NUM.
</br>
<br>printf "%x\n" $DECIMAL : Write a script that converts a number from base 10 to base 16.

    The number in base 10 is stored in the environment variable DECIMAL
    The script should display the number in base 16, followed by a new line
</br>
<br>tr 'A-Za-z' 'N-ZA-Mn-za-m' : Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.
</br>
<br>perl -lne 'print if $. % 2 == 1' : Write a script that prints every other line from the input, starting with the first line.</br>
<br>echo $(printf %o $(($((5#$(echo $WATER | tr 'water' '01234'))) + $((5#$(echo $STIR | tr 'stir.' '01234'))))) | tr '01234567' 'bestchol') : Write a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.

    WATER is in base water
    STIR is in base stir.
    The result should be in base bestchol
</br>
</em>
