import random
from datetime import datetime

def TimeTakenCalc(time):
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
        
    return "{} years, {} months, {} days, {} hours, {} minutes, {} seconds".format(years, months, days, hours, minutes, seconds)

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

aim = "LU"
curString = ""
furthest = ""

startTime = datetime.now()

print("Started At: " + str(startTime) + "\n")

failedAtt = 0
while curString != aim:
    curString += random.choice(alpha)

    index = 0
    for letter in curString:
        if not (letter == aim[index]):
            curString = ""
            failedAtt += 1
            break
        index += 1

    if len(curString) > len(furthest):
        furthest = curString
        print(curString)


endTime = datetime.now()
timeTaken = endTime - startTime
strTimeTaken = TimeTakenCalc(timeTaken.seconds)

print("\nFINISHED AT: " + str(endTime))
print("Failed Attempts: " + str(failedAtt))
print("TIME TAKEN: " + strTimeTaken)
