#Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. 
#Keep a limit to how far the program will go.
#https://www.mathscareers.org.uk/article/calculating-pi/
from math import pi
from decimal import Decimal, ROUND_DOWN

#gets the constant value of PI from the math module and creates a decimal object with this value
base = Decimal(10)
pi = Decimal(pi)
piApproximation = Decimal(3)

x = 2

isOdd = True
stillCalculating = True

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
        piApproximation += Decimal(4)/(x * (x+1) * (x+2))
        isOdd = False
    else:
        piApproximation -= Decimal(4)/(x * (x+1) * (x+2))
        isOdd = True
    x += 2
    if piApproximation.quantize(Decimal(n), rounding=ROUND_DOWN) - pi.quantize(Decimal(n), rounding=ROUND_DOWN) == 0:
        stillCalculating = False

print(Decimal(piApproximation).quantize(Decimal(n), rounding=ROUND_DOWN))