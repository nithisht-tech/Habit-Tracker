Tracker = {}
def Add():
    Num = int(input("Enter the no of habit:"))
    for i in range(Num):
        Habit = input("Enter the Habit:")
        Tracker[Habit] = False
def Disp():
    if Tracker=={}:
        print("Dictionary is empty!")
    else:
        for Habit, Status in Tracker.items():
            print(Habit, Status)
def Sta():
    Habit = input("Enter the name of the habit that you complete:")
    if Habit in Tracker:
        Tracker[Habit] = True
        print("Updated")
    else:
        print("Habit not found!")
def Del():
    Habit = input("Enter the name of the habit that you want to delete:")
    if Habit in Tracker:
        del Tracker[Habit]
        print("Deleted Successfully")
    else:
        print("Habit not found")
ch='y'
print("============Habit Tracker============")
while ch=='y' or ch=='Y':
    print("1.Add Habit")
    print("2.Display")
    print("3.Update the status")
    print("4.Delete Habit")
    print("5.Exit")
    opt = int(input("Enter the option:"))
    if opt==1:
        Add()
    elif opt==2:
        Disp()
    elif opt==3:
        Sta()
    elif opt==4:
        Del()
    elif opt==5:
        break
    else:
        print("Invalid option, Please select the option from 1 to 4")
    ch=input("Do you want to perform another operation(Y/N):")


    
