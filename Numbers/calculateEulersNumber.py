#Find Euler's number to the Nth Digit - Enter a number and have the program generate e up to that many decimal places.
#Keep a limit to how far the program will go.
#https://www.mathscareers.org.uk/article/calculating-eulers-constant-e/
from math import factorial
from decimal import Decimal, ROUND_DOWN

base = Decimal(10)
eulerApproximation = Decimal(2)

eulerApproximationString = str(eulerApproximation) + ".0"

decimalIndex = 2
denominator = 2
listOfApproximations = [eulerApproximationString, eulerApproximationString, eulerApproximationString, eulerApproximationString, eulerApproximationString]

stillCalculating = True

def moveApproximationValues(eulerApproximation):
    listOfApproximations[4] = listOfApproximations[3]
    listOfApproximations[3] = listOfApproximations[2]
    listOfApproximations[2] = listOfApproximations[1]
    listOfApproximations[1] = listOfApproximations[0]
    listOfApproximations[0] = str(eulerApproximation)

def checkForConvergence():
    for x in range(0, 4):
        if not listOfApproximations[x][decimalIndex] == listOfApproximations[x + 1][decimalIndex]:
            return False
    return True

#cycle to validate user input
while True:
    try:
        decimalPlaces = int(input("How many decimal places of Euler's number do you want? (up to 15 decimal places)\n"))
        break
    except:
        print("That is not a valid answer, please give a number\n")

if decimalPlaces > 0 and decimalPlaces < 16:
    n = str(1 + base**(-1 * decimalPlaces))
elif decimalPlaces >= 16:
    n = str(1 + base**(-1 * 15))
    decimalPlaces = 15
else:
    n = 1

while stillCalculating:
    
    eulerApproximation += Decimal(1)/factorial(denominator)
    moveApproximationValues(eulerApproximation)
    denominator += 1

    if checkForConvergence():
        decimalIndex += 1

    if decimalIndex - 2 == decimalPlaces:
        stillCalculating = False

print(Decimal(eulerApproximation).quantize(Decimal(n), rounding=ROUND_DOWN))