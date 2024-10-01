# Module 5 Lab-5
# Michaela Brady
# 9/27/2024
# This code calculates and prints bonus amounts for a retail company
# based on monthly sales figures and sales increases.
# The main function

def main():
    # Declare local variables
    monthlySales = 0  # Monthly sales amount
    storeAmount = 0   # Store bonus amount
    empAmount = 0     # Employee bonus amount
    salesIncrease = 0  # Percent of sales increase

    # Call to getSales(monthlySales)
    monthlySales = getSales("Enter the monthly sales amount: ")

    # Call to getIncrease(salesIncrease)
    salesIncrease = getIncrease("Enter the percent of sales increase: ")

    # Call to calcStoreBonus(storeAmount)
    storeAmount = calcStoreBonus(monthlySales)

    # Call to calcEmpBonus(empAmount)
    empAmount = calcEmpBonus(salesIncrease)

    # Call to printBonus(storeAmount, empAmount)
    printBonus(storeAmount, empAmount)

# This function gets the monthly sales
def getSales(prompt):
    monthlySales = float(input(prompt))
    return monthlySales

# This function gets the percent of increase in sales
def getIncrease(prompt):
    salesIncrease = float(input(prompt))
    salesIncrease = salesIncrease / 100
    return salesIncrease

# This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

# This function prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print('Congrats! You have reached the highest bonus amounts possible!')

# Call main
main()
