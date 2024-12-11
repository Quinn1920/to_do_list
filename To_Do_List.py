"""
Quinn Plummer
12/10/24
To Do List
This is a To Do List that you can add an item, remove an item, reset the list and show the list. The list is all different sports.
Period 1

"""
#Varibles
to_Do_List = ["Football", "Baseball", "Basketball", "Soccer"]
#My list is a gloabal variable that holds the to do items
# It is a list and the items

#functions
def addItem(item):
    to_Do_List.append(item)
def removeItem():
    for c in range(0, len(to_Do_List)):
        print(str(c + 1)+". " + to_Do_List[c])
        choice = input("Which item do you want to remove? ")
        if choice.isnumeric():
            choice = int(choice)
            if choice >= 0 and choice-1 <= len(to_Do_List):
                to_Do_List.pop(choice - 1)
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")
def have_fun():
    print("Have fun")
def resetList():
    # Reset the list
    to_Do_List.clear()
def printList():
    print(to_Do_List)
def show_menu():
    """This is a docString and it can be
    multiline
    The show menu function has no parameters and returns
    nothing it is used as the entry point to the
    to do program and displays a menu"""
    while True:
        print("Pick 1 to have fun")
        print("Pick 2 to do work")
        print("Pick 3 to quit")
       #Choice holds the input choice from the menu
        choice = input("Enter your choice: ")
        if choice == "1":
            have_fun()
        elif choice == "2":
            # do something
           pass
        elif choice == "3":
            print("Thank you for playing")
            break
        else:
            print("invalid choice")



show_menu()