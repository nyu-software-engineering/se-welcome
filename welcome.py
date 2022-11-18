#/usr/bin/env python

print('''
Welcome to Software Engineering!
* You are obviously running a Docker container instantiated from an image created by your professor.
* This output is the result of a python program that executed when the container launched.
* The Dockerfile used to create this image specific that this program should be run.\
''')

keep_on_loopin = True

while keep_on_loopin:
        print('''
Please select from the following choice menu items:
1) View the contents of the Dockerfile used to create this image
2) View the contents of the Python script
3) Exit
''')

        response = input("Which would you like to do? ")

        if response == "1":
                f = open("Dockerfile", "r")
                print("\nThe following are the contents of the Dockerfile used to make this image:\n")
                for line in f:
                        print("\t" + line.rstrip())
        elif response == "2":
                print("\nThe following are the contents of the Python program (me):\n")
                f = open("welcome.py", "r")
                for line in f:
                        print("\t" + line.rstrip())
        else:
                keep_on_loopin = False
                print("\nThanks for trying this out.  Bye!\n")
