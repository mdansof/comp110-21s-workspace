"""Tar Heels exercise redux as a structured program."""

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heel(choice))


# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heel(userVal:int)-> str:
if userVal % 2 == 0 and userVal % 7 == 0:
    return("TAR HEELS")
elif userVal % 2 == 0:
    return("TAR")
elif userVal % 7 == 0:
    return("HEELS")
else:
    return("CAROLINA")

if __name__ == "__main__":
    main()
