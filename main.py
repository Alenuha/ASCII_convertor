# this simple script converts text to ASCII characters and back
# uses UTF-16
from curses.ascii import isdigit

keep_going = True
while keep_going:

    option = input("Would you like to convert TO ASCII or FROM ASCII? Please type 'to' or 'from'\n").lower()

    if option == "to":
        string = input("Please, type your text:\n")
        for i in string:
            print(ord(i), end=" ")

    elif option == "from":
        string = input("Please type your characters, separated by SPACE\n")
        if string.isdigit():
            list_of_char = str.split(string)
            for char in list_of_char:
                char = int(char)
                print(chr(char), end=" ")
        else:
            print("This option only excepts natural integers. Please, try again\n")
            continue
    else:
        print("\nPlease, try again\n")
        continue

    check = True
    while check:
        double_check = input("\nWould you like to start again? y/n\n").lower()
        if double_check == "y":
            keep_going = True
            check = False
        if double_check == "n":
            print("Thank you! See you later!")
            keep_going = False
            check = False
        else:
            continue





