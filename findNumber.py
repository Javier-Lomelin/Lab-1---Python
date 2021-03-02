import random

from pip._vendor.distlib.compat import raw_input

number = random.randint(1, 30)
attempts = 0

file = "GuessingSteps.txt"
output = open("GuessingSteps.txt", "w")


def print_all(file_descriptor, text):
    file_descriptor.write(text + "\n")
    print(text)


print_all(output, "A random number between 1 and 30 was generated.")


def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


while True:
    print_all(output, " ")
    n = raw_input("Guess a number between 1 and 30: ")
    output.write("Input: " + n + "\n")

    if n == "exit":
        print_all(output, "Exit Program")
        break

    if not is_int(n):
        print_all(output, "Please input a number.\n")
        continue

    guess = int(n)

    if guess > number:
        print_all(output, "Guess a lower number.")
        attempts = attempts + 1
    elif guess < number:
        print_all(output, "Guess a higher number.")
        attempts = attempts + 1
    else:
        print_all(output, "You are correct! The random number was " + str(number))
        attempts = attempts + 1
        print_all(output, "You made " + str(attempts) + " guesses.")
        break

output.close()
