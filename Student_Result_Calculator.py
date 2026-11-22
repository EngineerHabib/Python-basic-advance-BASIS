import math


# Global List to Store Student Results
student_results = []


# Function 1: Calculate Total Marks
def calculate_total_marks(marks):
    total_marks = sum(marks)
    return total_marks


# Function 2: Calculate Average Marks
def calculate_average(total_marks, number_of_subjects):
    average_marks = total_marks / number_of_subjects
    return average_marks


# Function 3: Calculate Grade
def calculate_grade(average_marks):

    if average_marks >= 80:
        grade = "A+"

    elif average_marks >= 70:
        grade = "A"

    elif average_marks >= 60:
        grade = "B"

    elif average_marks >= 50:
        grade = "C"

    elif average_marks >= 33:
        grade = "D"

    else:
        grade = "F"

    return grade


# Function 4: Calculate Result Status
def calculate_result(marks):

    if any(mark < 33 for mark in marks):
        result = "Fail"

    else:
        result = "Pass"

    return result


# Function 5: Add Student Result
def add_student_result():

    print("\n========== ADD STUDENT RESULT ==========")

    # Take Student Information
    student_name = input("Enter Student Name: ").strip()
    roll_number = input("Enter Roll Number: ").strip()

    # Validate Student Information
    if not student_name or not roll_number:
        print("\nError: Student Name and Roll Number cannot be empty!")
        return

    # Input Marks of 5 Subjects
    marks = []

    subject_names = [
        "Python",
        "Database",
        "Networking",
        "Mathematics",
        "English"
    ]

    for subject in subject_names:

        try:
            subject_mark = float(input(f"Enter {subject} Marks (0-100): "))

            # Validate Subject Marks
            if not math.isfinite(subject_mark) or not (0 <= subject_mark <= 100):
                print("\nError: Marks must be between 0 and 100!")
                return

            marks.append(subject_mark)

        except ValueError:
            print("\nError: Please enter valid numeric marks!")
            return

    # Calculate Total Marks
    total_marks = calculate_total_marks(marks)

    # Calculate Average Marks
    average_marks = calculate_average(total_marks, len(marks))

    # Calculate Grade
    grade = calculate_grade(average_marks)

    # Calculate Pass/Fail Result
    result = calculate_result(marks)

    # Display Student Result
    print("\n========== STUDENT RESULT ==========")
    print("Student Name  :", student_name)
    print("Roll Number   :", roll_number)
    print("------------------------------------")

    for subject, mark in zip(subject_names, marks):
        print(f"{subject:<15}: {mark:g}")

    print("------------------------------------")
    print("Total Marks   :", total_marks)
    print("Average Marks :", round(average_marks, 2))
    print("Grade         :", grade)
    print("Result        :", result)
    print("====================================")

    # Store Student Result in List
    student_record = {
        "name": student_name,
        "roll": roll_number,
        "total": total_marks,
        "average": average_marks,
        "grade": grade,
        "result": result
    }

    student_results.append(student_record)

    print("\nSuccess: Student result added successfully!")


# Function 6: View All Student Results
def view_all_results():

    print("\n========== ALL STUDENT RESULTS ==========")

    if len(student_results) == 0:
        print("No student results found!")

    else:

        for index, record in enumerate(student_results, start=1):

            print(f"\n========== STUDENT {index} ==========")
            print("Student Name  :", record["name"])
            print("Roll Number   :", record["roll"])
            print("Total Marks   :", record["total"])
            print("Average Marks :", round(record["average"], 2))
            print("Grade         :", record["grade"])
            print("Result        :", record["result"])
            print("------------------------------------")

    # Display Total Number of Results
    print("\nTotal Results Saved:", len(student_results))


# Main Function: Menu-Driven Interface
def main():

    while True:

        print("\n======================================")
        print("       STUDENT RESULT CALCULATOR")
        print("======================================")
        print("1. Add Student Result")
        print("2. View All Results")
        print("3. Exit")
        print("======================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student_result()

        elif choice == "2":
            view_all_results()

        elif choice == "3":
            print("\nThank you for using Student Result Calculator!")
            print("Program exited successfully.")
            break

        else:
            print("\nInvalid Choice! Please select 1, 2, or 3.")


# Program Execution
if __name__ == "__main__":
    main()
