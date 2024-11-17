# Open the grades.txt file in read mode
try:
    with open("grades.txt", "r") as grades_file:
        # Read all grades into a list
        grades = grades_file.readlines()

    # Convert the grades from strings to floats
    grades = [float(grade.strip()) for grade in grades]

    # Display individual grades
    print("Grades:")
    for grade in grades:
        print(grade)

    # Calculate total, count, and average
    total = sum(grades)
    count = len(grades)
    average = total / count if count > 0 else 0

    # Display the results
    print(f"\nTotal: {total}")
    print(f"Count: {count}")
    print(f"Average: {average:.2f}")
except FileNotFoundError:
    print("The file 'grades.txt' was not found. Please ensure it exists in the current directory.")
except ValueError:
    print("The file contains invalid data that could not be converted to numbers.")

