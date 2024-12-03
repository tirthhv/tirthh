# Function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B+'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C+'
    elif marks >= 40:
        return 'C'
    else:
        return 'F'

# Function to create a marksheet
def create_marksheet():
    # Get student information
    name = input("Enter student's name: ")
    roll_no = input("Enter student's roll number: ")

    # Get marks for each subject
    subjects = ['Math', 'Science', 'English', 'History', 'Geography']
    marks = {}
    
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

    # Calculate total and percentage
    total_marks = sum(marks.values())
    percentage = (total_marks / 500) * 100
    
    # Display marksheet
    print("\n------ Marksheet ------")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_no}")
    print("\nSubjects and Marks:")

    for subject, mark in marks.items():
        grade = calculate_grade(mark)
        print(f"{subject}: {mark} - Grade: {grade}")

    print(f"\nTotal Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")

    # Determine the final grade
    if percentage >= 90:
        final_grade = 'A+'
    elif percentage >= 80:
        final_grade = 'A'
    elif percentage >= 70:
        final_grade = 'B+'
    elif percentage >= 60:
        final_grade = 'B'
    elif percentage >= 50:
        final_grade = 'C+'
    elif percentage >= 40:
        final_grade = 'C'
    else:
        final_grade = 'F'

    print(f"Final Grade: {final_grade}")
    print("----------------------------")

# Run the marksheet function
create_marksheet()
