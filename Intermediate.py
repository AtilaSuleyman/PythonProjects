"""
1.
A simple game of blackjack
"""

def blackjack(firstNum, secondNum):
    firstPlayer = firstNum
    secondPlayer = secondNum
    firstResult = 0
    secondResult = 0
    finalResult = 0
    if(firstPlayer > 21 and secondPlayer > 21):
        return finalResult
    else:
        if(firstPlayer > 21):
            finalResult = secondPlayer
        elif(secondPlayer > 21):
            finalResult = firstPlayer
        else:
            firstResult = 21 - firstPlayer
            secondResult = 21 - secondPlayer
            if(firstResult < secondResult):
                finalResult = firstPlayer
            else:
                finalResult = secondPlayer
    return finalResult

result = blackjack(21, 16)
print (result)

print("------------------------------------------------------")

"""
2.
only return the sum of unique numbers given
"""
def uniqueSum(firstNo, secondNo, thirdNo):
    if (firstNo == secondNo and firstNo == thirdNo):
        return 0;
    elif (firstNo == thirdNo):
        return secondNo;
    elif (secondNo == thirdNo):
        return firstNo;
    elif (firstNo == secondNo): 
        return thirdNo;
    else: 
        return firstNo + secondNo + thirdNo;
    
result = uniqueSum(3,3,1)
print (result)

print("------------------------------------------------------")
        
"""
3.
Given an integer value and a Boolean value, temperature and isSummer, 
if temperature is between 60 and 90 (inclusive), unless its summer where 
the upper limit is 100 instead of 90. Return true if the temperature falls
within the range, false otherwise.
"""    
def tooHot(temp, isSummer):
    tooHot = False;
    if (isSummer):
        if (temp > 59 and temp < 101):
            tooHot = True;
    else:
        if (temp > 59 and temp < 91):
            tooHot = True;
    print (tooHot);
    return tooHot;  

tooHot(91, True)

print("------------------------------------------------------")