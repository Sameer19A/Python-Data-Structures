#Task 21
#Compulsory Task


#InputName = ""
NamesList = []   # list to store the names
InputName = input("Enter your name: ")
while InputName.lower() != "john":
    NamesList.append(InputName)
    InputName = input("Enter your name: ")


print("Incorrect names: " + str(NamesList[0:len(NamesList)]))   #convert a list to string and display
