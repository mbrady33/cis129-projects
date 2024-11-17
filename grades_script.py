# Open the file in write mode
with open("grades.txt", "w") as grades_file:
    print("Enter grades one by one. Enter -1 to finish.")
    
    while True:
        try:
            # Prompt the user for a grade
            grade = input("Enter a grade: ")
            
            # Convert the input to a number
            grade = float(grade)
            
            # Check for the sentinel value
            if grade == -1:
                print("Finished entering grades.")
                break
            
            # Write the grade to the file
            grades_file.write(f"{grade}\n")
        except ValueError:
            print("Invalid input. Please enter a numeric grade or -1 to finish.")

