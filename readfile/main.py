# Creating an python to read an file exist or not

import os

file = "tio.txt"

if os.path.exists(file):
    print("File is ready!")

    if os.path.isfile(file):
        print("The path was file!")
    elif os.path.isdir(file):
        print("The path was an directory!")
    else:
        print("is that a file!")
else:
    print("File is not exists")
