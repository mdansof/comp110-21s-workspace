"""An exercise in remainders and boolean logic."""

__author__ = "730316345"


# Begin your solution here...
userInput = input("Please enter an integer: ")
userVal = int(userInput)
if userVal % 2 == 0 and userVal % 7 == 0:
    print("TAR HEELS")
# elif userVal % 2 == 0:
#     print("TAR")
# elif userVal % 7 == 0:
#     print("HEELS")
# else:
#     print("CAROLINA")
else:
    if userVal % 2 == 0:
        print("Tar")
    else:
        if userVal % 7 == 0:
            print("heels")
        else:
            print("caro")

