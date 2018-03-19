# Import packages
import random  # Used for picking random letters
import subprocess  # Used to interact with OS to run copy function
import time  # Used to sleep shell to keep window open
import os  #Used to deetct OS and copy on MacOS


# Function to copy string to user's clipboard
def copy2clip(txt):
    cmd = 'echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


# Detect OS and copy to clipboard
def copy(text):
    if os.name == 'nt': # If os is windows
        copy2clip(text)
        print('This has been copied to your clipboard!')
    elif os.name == 'posix': # If os is MacOS
        os.system("echo '%s' | pbcopy" % text) # Runs command to copy to clipboard on MacOS
        print('This has been copied to your clipboard!')
    else: # If unable to detect os
        print('Unable to autocopy to clipboard')


# Specifies what letters to be used
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Takes user input
needed = input("Please enter the length of string required: ")

# Initialises Variable
needed = int(needed)-1
start = (random.choice(letters))
string = start

# Generates and appends remaining needed characters
for x in range(0, needed):  # Repeats chunk of code for now much 'needed' is
    selected = (random.choice(letters))
    string = string+selected  # Appends the letter to the rest of the 'string'

# Print out final string
print('===============================================================================================================')
print('Final String is:')
print(string)
copy(string)  # Copies string to user's clipboard
print('===============================================================================================================')
time.sleep(5)  # Used to keep window open for 5 sec after use
