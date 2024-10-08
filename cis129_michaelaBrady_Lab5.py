# Lab 5 The Bottle Return Program
# Name: Michaela Brady
# Date: 10/7/24
# Description: This program calculates the total number of bottles returned over seven days
# and computes the total payout at $0.10 per bottle.

def get_bottles():
    NBR_OF_DAYS = 7  # Constant for the number of days

    while True:  # Loop to allow multiple weeks of data entry
        total_bottles = 0  # Accumulator for total bottles
        counter = 0  # Counter for days

        # Loop through each day to get the number of bottles returned
        while counter < NBR_OF_DAYS:
            try:
                today_bottles = int(input(f"Enter number of bottles returned for day #{counter + 1}: "))
                if today_bottles < 0:
                    print("Please enter a non-negative number.")
                    continue  # Skip to the next iteration if the input is negative
                total_bottles += today_bottles  # Accumulate total bottles
                counter += 1  # Increment the counter
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Calculate total payout
        total_payout = total_bottles * 0.10
        print(f"\nTotal bottles returned: {total_bottles}")
        print(f"Total amount paid out: ${total_payout:.2f}\n")

        # Ask if the user wants to enter more data
        more_data = input("Do you have more data to enter? (yes/no): ").strip().lower()
        if more_data != 'yes':
            print("Thank you for using the bottle tracking program.")
            break  # Exit the loop if the user does not want to continue

def main():
    get_bottles()  # Call the get_bottles function to start the program

# Start the program by calling the main function
main()
