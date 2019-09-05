#Task 22
#Compulsory Task 1
#This program takes the given, poorly written string/message and changes it to a more intelligent sentence.

Message = "HI:HOW:R:U:TODAY"

Message = Message.split(':')   # split the message into pieces using the colons
#print(Message[0])

#converting the words to lowercase using one line
#can also do it using the for loop seprately with 2 lines of code
LowCaseMessage = [word.lower() for word in Message]   

#print(LowCaseMessage)


#print(Message[0])
#print(Message[-1])

#Assign the 1st word and last word to a string variable:
Firstword = LowCaseMessage[0]
Lastword = LowCaseMessage[-1]

#now we use string indexing to capitalise the 1st letter and we add a fullstop to the last word
Firstword = Firstword[0].upper()+ Firstword[1]  #use string indeces to capitalise the first letter
Lastword = Lastword + "."

#print(Firstword)
#print(Lastword)

LowCaseMessage[0] = Firstword   # replace the words in the low case message with the altered words
LowCaseMessage[-1] = Lastword

print(LowCaseMessage)
