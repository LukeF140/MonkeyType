from datetime import datetime
import random

# Convert Seconds into a string
def TimeTakenCalc(time):
    millenias = time // 311040000000000
    time = time % 311040000000000
    centurys = time // 3110400000000
    time = time % 3110400000000
    decades = time // 3110400000
    time = time % 3110400000
    years = time // 31104000
    time = time % 31104000
    months = time // 2592000
    time = time % 2592000
    days = time // 86400
    time = time % 86400
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
        
    return "{} millenias, {} centurys, {} decades, {} years, {} months, {} days, {} hours, {} minutes, {} seconds".format(millenias, centurys, decades, years, months, days, hours, minutes, seconds)


print("THIS IS AN APPROXIMATION OF HOW LONG IT WOULD TAKE FOR THIS COMPUTER TO SPELL OUT THE TARGET  STRING")
print("AS WITH RANDOM EVENTS IT COULD HAPPEN MUCH FASTER OR SLOWER THIS IS JUST A MATHMATICAL WAY OF TRYING TO ASSUME WHEN IT WILL OCCUR")
print("\n")

# Alphabet variations for whatever is needed
alpha = "QWERTYUIOPLKJHGFDSAZXCVBNM "
alphaNum = "QWERTYUIOPLKJHGFDSAZXCVBNM1234567890 "
alphaNumPunc = "QWERTYUIOPLKJHGFDSAZXCVBNM1234567890!\"£$%^&*()-_=+\|/?><,.¬`:;@'~#[]{} "

# Target String
tarStr = ""


# Get User Input
tarStr = input("Please enter the string: ").upper()
using = 0
for letter in tarStr:
        if letter in alphaNumPunc and not(letter in alphaNum) and not(letter in alpha):
            using = 2
        elif using < 1 and letter in alphaNum and not(letter in alpha):
            using = 1
        elif using < 0:
            using = 0


# Percentage chance that the string is created from random letters
if using == 0:
    perGet = (1/len(alpha))**len(tarStr)
elif using == 1:
    perGet = (1/len(alphaNum))**len(tarStr)
elif using == 2:
    perGet = (1/len(alphaNumPunc))**len(tarStr)
else:
    print("SOMETHING BROKE!!")
    
print("Percentage Chance String Occurs On A Pass: " + str(perGet) + "%")


# Number of times it will take (approx.) for the string to be printed
numTimes = 100/perGet
print("Passes Needed Until String Is Printed: " + str(int(numTimes)))


# Work out how long it takes for the computer to get 1000000 (million) letters
startTime = datetime.now()
letters = 0
while letters < 1000000:
    random.choice(alpha)
    letters += 1
finishTime = datetime.now()
timeTaken = finishTime - startTime
timeLet = ((timeTaken.seconds) / 1000000) # How long to get a letter
if len(tarStr) > 50:
    timeForString = timeLet / (len(tarStr)/(len(tarStr)/5)) # Adjust to the size of string (amount if characters needed)


timeNeeded = int(numTimes * timeLet) # Work out the amount of time needed for random letters to make the sentence
print("Time Needed: " + TimeTakenCalc(timeNeeded))
