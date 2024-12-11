
# This is how you make a list
myList = ["thing 1", "thing 2", "thing 3", "thing 4"]
# This is how you access individual items in the list
print(myList[1])
print(myList[3])
# This is how you add to the end of the list
myList.append("Thing 5")
# This is how you print the entire list
print(myList)
# This is how you remove items using the index
myList.pop(2)
print(myList)

def have_fun():
    pass
def show_menu():
    while True:
        print("Pick 1 to have fun")
        print("Pick 2 to do work")
        print("Pick 3 to quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            have_fun()
        elif choice == "2":
            #do something
            pass
        elif choice == "3":
            print("Thank you for playing")
                break
    else:
        print("invalid choice")
