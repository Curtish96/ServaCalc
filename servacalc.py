## ServaCalc, a simple calculation tool used to determine the cost of running a physical server over the course of a month by inputting specifications.

try:
    print("Welcome to ServaCalc, the simple server running costs calculation tool. I need to take a few bits of information from you.\n")
    towerCost = float(input("What is the cost of your tower unit in pounds and pence?\n"))
    wattValue = int(input("How many watts does your tower unit use? See the manufacturer's website for details.\n"))
    electricityCost = float(input("Please enter the cost of your electricity in the form of pence per KWh. Check your energy provider for details.\n"))


except ValueError:
    print("Please only enter digits.")


else:

    kwhHour = wattValue * 24 / 1000
    kwhHourCost = float(kwhHour * electricityCost)
    totalcostMonth = float(kwhHourCost * 24 * 365 / 12)

    print(f"Your initial setup costs are £{towerCost:,.2f}".replace('$-', '-$'))
    print(f"Your total monthly server running costs are £{totalcostMonth/100:,.2f}".replace('$-', '-$'))
    
    ## Calculations.

    # 1000 watts = 1kwh (kilowatt hour) so the full calculation would be the wattValue * hours / 1000 to get the kwh value. 
    # For example: 250 watts * 5 hours in a day = 1.25kwh per day.
    # Then to find the total cost, multiply the value of a server KWh by the cost of electricity per KWh.
    # In this project calculation, we will assume the server is running 24 hours a day 365 days a year, as an identity solution should be. We're doing the cost by month, so...
    # The overall math is (cost of KWh * 24 (hours) * 365 (days) / 12 (months).