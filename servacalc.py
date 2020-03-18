## ServaCalc, a simple calculation tool used to determine the cost of running a physical server over the course of a month by inputting specifications.

try:
    towerCost = float(input("What is the cost of your tower unit?"))

except ValueError:
    print("Please only enter digits.")

else:
    ## To be continued