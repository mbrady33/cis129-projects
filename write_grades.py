import csv

# Open the grades.csv file in write mode
with open("grades.csv", "w", newline="") as csvfile:
    # Create a writer object
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])
    
    print("Enter student records. Type 'done' as the first name to stop.")
    
    while True:
        # Prompt for student's first name
        firstname = input("Enter first name (or 'done' to finish): ").strip()
        if firstname.lower() == "done":
            print("Finished entering records.")
            break
        
        # Prompt for student's last name
        lastname = input("Enter last name: ").strip()
        
        try:
            # Prompt for three exam grades
            exam1 = int(input("Enter exam 1 grade: "))
            exam2 = int(input("Enter exam 2 grade: "))
            exam3 = int(input("Enter exam 3 grade: "))
            
            # Write the student's record to the CSV file
            writer.writerow([firstname, lastname, exam1, exam2, exam3])
        except ValueError:
            print("Invalid input. Please enter integer values for grades.")

