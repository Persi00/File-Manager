import os
os.system("cls")
from termcolor import colored as c

path = os.getcwd()
error = ""

while True:
    items = os.listdir(path)
    i=2
    print("Your current directory: " + path)
    print("0) " + c("exit", "magenta") + "\n1) " + c("..", "green"))
    for item in items:
        color = "white"
        if os.path.isdir(os.path.abspath(item)):
            color = "green"
        elif os.path.isfile(os.path.abspath(item)):
            color = "cyan"
        else:
            color = "yellow"
        print(str(i) + ") " + c(item, color))
        i+=1
    number = int(input(error + "Choose the number: "))
    if number == 0:
        exit()
    elif number == 1:
        path = os.path.abspath(path + "\\..")
        error = ""
    elif number > i-1 and number < 0:
        error = c("incorrect number\n", "red")
    else:
        if os.path.isfile(os.path.abspath(items[number-2])):
            os.system("start " + items[number-2])
        else:
            path = os.path.abspath(path + "\\" + items[number-2])
        error = ""
    os.system("cls")