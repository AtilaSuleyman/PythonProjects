"""
1.
A simple Hello World program that prints Hello World!
"""
print ("Hello World!")
print("------------------------------------------------------")

"""
2.
Stores "Hello World!" in a variable and prints it out
"""

HelloWorld = "Hello World!"
print (HelloWorld)

print("------------------------------------------------------")
"""
3.
A function that takes two numbers and prints them out
"""
def sumNumbers(firstNum, secondNum):
    print (firstNum + secondNum)
    
sumNumbers(2, 3)

print("------------------------------------------------------")

"""
4.
A function that takes two numbers and a boolean.
Prints the some of the two numbers if the boolean evaluates to true, multiplies them otherwise
"""

def sumOrMultiplyNumbers(firstNum, secondNum, wantToSum):
    if(wantToSum):
        print (firstNum + secondNum)
    else:
        print (firstNum * secondNum)
             
sumOrMultiplyNumbers(2, 3, False)

print("------------------------------------------------------")

"""
5.
A function that takes two numbers and a boolean.
Prints the some of the two numbers if the boolean evaluates to true, multiplies them otherwise.
Improved so that it takes into account 0 when multiplying
"""

def sumOrMultiplyNumbersTwo(firstNum, secondNum, wantToSum):
    if(wantToSum):
        print (firstNum + secondNum)
    elif(firstNum == 0):
        print (secondNum)
    elif(secondNum == 0):
        print (firstNum)
    else:
        print (firstNum * secondNum)
             
sumOrMultiplyNumbersTwo(3, 9, False)

print("------------------------------------------------------")

"""
6.
A function that takes two numbers and a boolean.
Prints the some of the two numbers if the boolean evaluates to true, multiplies them otherwise.
Improved so that it takes into account 0 when multiplying
uses a loop to generate input of which the users chosen number will be sum/times by
"""

def sumOrMultiplyNumberTenTimes(number, wantToSum):
    for i in range (0, 10):
        sumOrMultiplyNumbersTwo(number, i, wantToSum)
        
sumOrMultiplyNumberTenTimes(2, True)

print("------------------------------------------------------")

"""
7.
A function that takes two numbers and a boolean.
Prints the some of the two numbers if the boolean evaluates to true, multiplies them otherwise.
Improved so that it takes into account 0 when multiplying
uses a loop and a list to generate input of which the users chosen number will be sum/times by
"""
numList = [2,21,4,5,14,8,3,5,6,25]
def sumOrMultiplyFromList(userNum, wantToSum):
    for num in numList:
        sumOrMultiplyNumbersTwo(userNum, num, wantToSum)

sumOrMultiplyFromList(2, True)

print("------------------------------------------------------")
        
"""
8.
prints out all elements of a list
"""    

def printListItems():
    for num in numList:
        print (num)

printListItems()

print("------------------------------------------------------")

"""
8.
appends numbers 0-9 to a list and prints them out
then it gets each number in the list, times it by 10 and stores it back.
Prints out theb stored number
"""   

def appendAndPrintOut():
    #listOfNumbers = [for i range (0, 10)]
    listOfNumbers = []
    for i in range (0,10):
        listOfNumbers.append(i)
        print (i)
    print("----")
    for i in range (0, 10):
        listOfNumbers[i] = listOfNumbers[i]*10
        print (listOfNumbers[i])

appendAndPrintOut()

print("------------------------------------------------------")

"""
9.
appends numbers 0-9 to a list and prints them out
then it gets each number in the list, times it by 10 and stores it back.
Prints out theb stored number
"""   
def takingUserInput():
    print("please type in the amount of numbers you would like in order to start")
    numberOfListItems = int(input())
    listNums = [i for i in range(numberOfListItems)]
    for num in listNums:
        print(num)
        
takingUserInput()