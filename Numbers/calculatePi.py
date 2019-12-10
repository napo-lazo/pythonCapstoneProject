#Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. 
#Keep a limit to how far the program will go.
#https://www.mathscareers.org.uk/article/calculating-pi/
from decimal import Decimal, ROUND_DOWN

base = Decimal(10)
piApproximation = Decimal(3)

piApproximationString = str(piApproximation) + ".0"

decimalIndex = 2
listOfApproximations = [piApproximationString, piApproximationString, piApproximationString, piApproximationString, piApproximationString]
numerator = 2

isOdd = True
stillCalculating = True

def moveApproximationValues(piApproximation):
    listOfApproximations[4] = listOfApproximations[3]
    listOfApproximations[3] = listOfApproximations[2]
    listOfApproximations[2] = listOfApproximations[1]
    listOfApproximations[1] = listOfApproximations[0]
    listOfApproximations[0] = str(piApproximation)

def checkForConvergence():
    for x in range(0, 4):
        if not listOfApproximations[x][decimalIndex] == listOfApproximations[x + 1][decimalIndex]:
            return False
    return True

#cycle to validate user input
while True:
    try:
        decimalPlaces = int(input("How many decimal places of PI do you want? (up to 15 decimal places)\n"))
        break
    except:
        print("That is not a valid answer, please give a number\n")

if decimalPlaces > 0 and decimalPlaces < 16:
    n = str(1 + base**(-1 * decimalPlaces))
elif decimalPlaces > 15:
    n = str(1 + base**(-1 * 15))
else:
    n = 1

while stillCalculating:
    if isOdd:
        piApproximation += Decimal(4)/(numerator * (numerator+1) * (numerator+2))
        moveApproximationValues(piApproximation)
        isOdd = False
    else:
        piApproximation -= Decimal(4)/(numerator * (numerator+1) * (numerator+2))
        moveApproximationValues(piApproximation)
        isOdd = True
    numerator += 2
    
    if checkForConvergence():
        decimalIndex += 1

    if decimalIndex - 2 == decimalPlaces:
        stillCalculating = False

print(Decimal(piApproximation).quantize(Decimal(n), rounding=ROUND_DOWN))