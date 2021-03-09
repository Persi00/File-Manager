import os
os.system("cls")
from termcolor import colored as c

path = os.getcwd()
error = ""

while True:
    os.system("cls")
    items = os.listdir(path)
    i=3
    print("Your current directory: " + path)
    print("0) " + c("exit", "magenta") + "\n1) " + c(".", "green") + "\n2) " + c("..", "green"))
    for item in items:
        color = "white"
        if os.path.isdir(os.path.abspath(item)):
            color = "green"
        elif os.path.isfile(os.path.abspath(item)):
            color = "cyan"
        elif os.path.islink(os.path.abspath(item)):
            color = "yellow"
        print(str(i) + ") " + c(item, color))
        i+=1
    number = int(input(error + "Choose the number: "))
    if number == 0:
        os.system("cls")
        exit()
    elif number == 1:
        path = os.path.abspath(os.path.join(path + "."))
        error = ""
    elif number == 2:
        path = os.path.abspath(os.path.join(path, ".."))
        error = ""
    elif (number >= i) or (number < 0):
        error = c("incorrect number\n", "red", attrs=['bold'])
    else:
        if os.path.isfile(os.path.abspath(items[number-3])):
            os.system("start " + items[number-3])
        else:
            path = os.path.abspath(os.path.join(path, items[number-3]))
        error = ""