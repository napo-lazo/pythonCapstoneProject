#Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. 
#Keep a limit to how far the program will go.
#https://www.mathscareers.org.uk/article/calculating-pi/
from math import pi
from decimal import Decimal, ROUND_DOWN

#gets the constant value of PI from the math module and creates a decimal object with this value
pi = Decimal(pi)
piAproximation = 3
isOdd = True
stillCalculating = True
x = 2

#cycle to validate user input
while True:
    try:
        decimalPlaces = float(input("How many decimal places of PI do you want?\n"))
        break
    except:
        print("That is not a valid answer, please give a number\n")

if(decimalPlaces > 0 and decimalPlaces < 16):
    n = str(1 + 10**(-1 * decimalPlaces))
else:
    n = 1

while stillCalculating:
    if isOdd:
        piAproximation += 4/(x * (x+1) * (x+2))
        isOdd = False
    else:
        piAproximation -= 4/(x * (x+1) * (x+2))
        isOdd = True
    x += 2
    if Decimal(piAproximation).quantize(Decimal(n), rounding=ROUND_DOWN) - Decimal(pi).quantize(Decimal(n), rounding=ROUND_DOWN) == 0:
        stillCalculating = False

print(Decimal(piAproximation).quantize(Decimal(n), rounding=ROUND_DOWN))
