#Task 21
#Optional Task 1

friends_names = []  #list containing friends names
friends_ages = []   #list containing friends ages
for i in range(0,3):
    FullName = input("Please enter your full name:\t")
    Age = input("Please enter your age:\t")  #will notcast to int as we not using it for calculations(as yet)
    friends_names.append(FullName)   # add the entered full name to the friends name list
    friends_ages.append(Age)   # add the entered age to the friends ages list

print("\n")
print(friends_names[0])   # print name of first friend
print(friends_names[-1])   # print name of last friend
print("The length of the list is " + str(len(friends_names)))

##print(friends_names)
##print(friends_ages)

