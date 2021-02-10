"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: 
def fortune_cookie() -> str:
    "returns random string"
    randNum = randint(1, 100)
if randNum < 30:
    return("A beautiful, smart and loving person will be coming into your life.")
else: 
    if randNum < 70:
        return("Your life will be happy and peaceful.")
    elif randNum < 90:
        return("Soon life will become more interesting.")
    elif randNum < 100:
        return("Beware the snakes in the grass.")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
