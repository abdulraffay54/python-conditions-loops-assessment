# Student Scholarship Eligibility System

# Eligibility rules (named variables instead of magic numbers)
MIN_MARKS = 80
MIN_ATTENDANCE = 85
MAX_MONTHLY_INCOME = 50000
FULL_SCHOLARSHIP_MARKS = 90
MIN_PERCENTAGE = 0
MAX_PERCENTAGE = 100

print("\n==== Student Scholarship Eligibility System ====")

# Step 1: Collect student information as text
student_name = input("\nEnter student name: ").strip()
marks_text = input("Enter academic marks (%): ").strip()
attendance_text = input("Enter attendance percentage (%): ").strip()
income_text = input("Enter monthly family income (Rs.): ").strip()

# Step 2: Validate numeric text before conversion
is_marks_number = marks_text.replace(".", "", 1).isdecimal()
if marks_text.startswith("-"):
    is_marks_number = marks_text[1:].replace(".", "", 1).isdecimal()

is_attendance_number = attendance_text.replace(".", "", 1).isdecimal()
if attendance_text.startswith("-"):
    is_attendance_number = attendance_text[1:].replace(".", "", 1).isdecimal()

is_income_number = income_text.replace(".", "", 1).isdecimal()
if income_text.startswith("-"):
    is_income_number = income_text[1:].replace(".", "", 1).isdecimal()

# Step 3: Validate all information
if student_name == "":
    print("Invalid Input! Student name cannot be empty.")

elif not is_marks_number:
    print("Invalid Input! Academic marks must be a number.")

elif not is_attendance_number:
    print("Invalid Input! Attendance must be a number.")

elif not is_income_number:
    print("Invalid Input! Monthly family income must be a number.")

else:
    academic_marks = float(marks_text)
    attendance_percentage = float(attendance_text)
    monthly_family_income = float(income_text)

    if academic_marks < MIN_PERCENTAGE or academic_marks > MAX_PERCENTAGE:
        print("Invalid Input! Marks must be between 0 and 100.")

    elif (attendance_percentage < MIN_PERCENTAGE
          or attendance_percentage > MAX_PERCENTAGE):
        print("Invalid Input! Attendance must be between 0 and 100.")

    elif monthly_family_income < 0:
        print("Invalid Input! Income cannot be negative.")

    else:
        # Step 4: Display student information
        print("\n==== Scholarship Evaluation Report ====")
        print("\nStudent Name:", student_name)
        print(f"Academic Marks: {academic_marks:.1f} %")
        print(f"Attendance: {attendance_percentage:.1f} %")
        print(f"Monthly Family Income: Rs. {monthly_family_income:.2f}")

        # Step 5: Check eligibility
        if (academic_marks >= MIN_MARKS
                and attendance_percentage >= MIN_ATTENDANCE
                and monthly_family_income <= MAX_MONTHLY_INCOME):
            if academic_marks >= FULL_SCHOLARSHIP_MARKS:
                scholarship_type = "Full Scholarship"
            else:
                scholarship_type = "Partial Scholarship"

            print("\nScholarship Status: Eligible")
            print("Scholarship Type:", scholarship_type)

        else:
            print("\nScholarship Status: Not Eligible")
            print("\nReason for Ineligibility:")

            if academic_marks < MIN_MARKS:
                print(f"- Academic marks are below {MIN_MARKS}%.")

            if attendance_percentage < MIN_ATTENDANCE:
                print(f"- Attendance is below {MIN_ATTENDANCE}%.")

            if monthly_family_income > MAX_MONTHLY_INCOME:
                print(
                    "- Monthly family income exceeds "
                    f"Rs. {MAX_MONTHLY_INCOME:,}."
                )

        print("====================================")
