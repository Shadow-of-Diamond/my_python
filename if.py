#!/usr/bin/python
# Filename: if.py
number = 23
guess = int(input('Enter an integer: '))
if guess == number:
    print ('Congratulations, you guessed it.') # New block starts here
    print ("(but you do not win any prizes!)" )# New block ends here
elif guess < number:
    print ('No, it is a little higher than that') # Another block
# You can do whatever you want in a block ...
else:
    print ('No, it is a little lower than that')
# you must have guess > num ber to reach here
print ('Done')
# This last statem ent is always executed, after the if statem ent is executed