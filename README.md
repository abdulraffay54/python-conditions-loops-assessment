# Python Conditions & Loops Assessment

## Project Introduction and Overview

This project contains two beginner-friendly Python programs created for the
Conditions & Loops Assessment. Both programs run in the terminal and ask the
user to enter values while the program is running.

The project demonstrates only the topics required by the assessment:

- Conditional statements: `if`, `elif`, and `else`
- `for` loops and `range()`
- Conditions inside loops
- Counters and accumulators

### Project Files

| File | Purpose |
|---|---|
| `student_scholarship_system.py` | Checks whether a student is eligible for a scholarship. |
| `pharmacy_inventory_system.py` | Processes pharmacy sales and prints a daily sales report. |
| `README.md` | Explains the project and how to run it. |

## Explanation of Both Programs

### Task 1: Student Scholarship Eligibility System

**File:** `student_scholarship_system.py`

This program checks whether a student is eligible for a university scholarship.
It asks for the student's name, academic marks, attendance percentage, and
monthly family income.

The program validates the input before showing the result:

- The name cannot be empty.
- Marks and attendance must be numbers from 0 to 100.
- Monthly income must be a number and cannot be negative.
- Text such as `abc`, `nan`, or `inf` is rejected.

If the input is invalid, the program prints a clear message and stops without a
Python error traceback.

If the input is valid, the program checks these rules:

| Requirement | Rule |
|---|---|
| Academic marks | At least 80% |
| Attendance | At least 85% |
| Monthly family income | Rs. 50,000 or less |
| Full Scholarship | All rules are met and marks are 90% or above |
| Partial Scholarship | All rules are met and marks are 80% to 89% |

The program can produce three results:

- **Full Scholarship:** the student meets all requirements and has 90% or more
  marks.
- **Partial Scholarship:** the student meets all requirements and has 80% to
  89% marks.
- **Not Eligible:** at least one requirement is not met. The program lists every
  reason that applies.

### Task 2: Smart Pharmacy Inventory & Sales Management System

**File:** `pharmacy_inventory_system.py`

This program manages pharmacy sales and calculates the total daily revenue. It
first asks how many medicines you want to process. The number must be a whole
number of at least 1.

For each medicine, the program asks for:

1. Medicine name
2. Available stock
3. Price per unit (Rs.)
4. Quantity sold

The program validates each value before using it:

- The medicine name cannot be empty.
- Stock and quantity sold must be whole numbers.
- Price must be a number.
- Numeric values cannot be negative.
- Text such as `abc`, `nan`, or `inf` is rejected.

If one medicine has invalid input, the program prints an error for that
medicine and moves on to the next one.

For each valid medicine, the program:

- Checks whether the requested quantity is available.
- Rejects the sale if the quantity sold is greater than the available stock.
- Calculates the sales amount and the remaining stock.
- Adds the sales amount to the total revenue.
- Shows a low-stock warning when fewer than 10 units remain.
- Counts the medicine for restocking when the remaining stock is below 10.

At the end, the program prints a daily sales report with these values:

| Report line | Meaning |
|---|---|
| Total Medicines Entered | The number of medicine entries you asked to process. |
| Medicines Successfully Processed | The number of sales that completed successfully. |
| Total Pharmacy Revenue | The total money earned from successful sales. |
| Medicines Requiring Restocking | Successful sales that left fewer than 10 units in stock. |

## Python Concepts Covered

- `input()` and `print()`
- Variables and data types
- Type conversion with `int()` and `float()`
- Conditional statements: `if`, `elif`, and `else`
- Comparison operators
- Logical operators: `and` and `or`
- `for` loops and `range()`
- Conditions inside loops
- Counters and accumulators
- Basic input validation
- Simple string checks such as `.strip()`, `.isdecimal()`, `.replace()`, and
  `.startswith()`
- Formatted output with f-strings

## Instructions for Executing Both Programs

### 1. Check That Python Is Installed

Run this command in your terminal or command prompt:

```bash
python --version
```

You need Python 3.6 or newer. If `python` does not work, try:

```bash
python3 --version
```

On Windows, you can also try:

```bash
py --version
```

### 2. Download the Project

You need a copy of the project on your computer.

**Option A: Clone with Git**

```bash
git clone https://github.com/abdulraffay54/python-conditions-loops-assessment
cd python-conditions-loops-assessment
```

**Option B: Download the ZIP file**

1. Open the repository page on GitHub.
2. Click the **Code** button and choose **Download ZIP**.
3. Extract the ZIP file.
4. Open a terminal in the extracted project folder.

### 3. Run Task 1

Run this command from the project folder:

```bash
python student_scholarship_system.py
```

If `python` is not found, use:

```bash
python3 student_scholarship_system.py
```

### 4. Run Task 2

Run this command from the project folder:

```bash
python pharmacy_inventory_system.py
```

If `python` is not found, use:

```bash
python3 pharmacy_inventory_system.py
```

### Notes

- The programs are interactive. After you start one, it waits for you to enter
  the requested values and press Enter.
- The programs do not save data to a file. Everything you enter is lost when the
  program ends.
- Each program runs once and then exits. To use it again, run the command again.
- You can stop a program at any time with `Ctrl+C`.

## Sample Input/Output for Both Applications

### Task 1: Scholarship System

**Sample Input:**

```text
Enter student name: Ali
Enter academic marks (%): 95
Enter attendance percentage (%): 90
Enter monthly family income (Rs.): 30000
```

**Sample Output:**

```text
==== Student Scholarship Eligibility System ====

==== Scholarship Evaluation Report ====

Student Name: Ali
Academic Marks: 95.0 %
Attendance: 90.0 %
Monthly Family Income: Rs. 30000.00

Scholarship Status: Eligible
Scholarship Type: Full Scholarship
====================================
```

**Invalid input example:**

```text
Enter student name: Ali
Enter academic marks (%): abc
Enter attendance percentage (%): 90
Enter monthly family income (Rs.): 30000
Invalid Input! Academic marks must be a number.
```

### Task 2: Pharmacy System

**Sample Input:**

```text
Enter the number of medicines: 2

---- Medicine 1 ----
Enter medicine name: Panadol
Enter available stock: 50
Enter price per unit (Rs.): 30
Enter quantity sold: 45

---- Medicine 2 ----
Enter medicine name: Calpol
Enter available stock: 40
Enter price per unit (Rs.): 50
Enter quantity sold: 10
```

**Sample Output:**

```text
==== Smart Pharmacy Inventory & Sales Management System ====

---- Medicine 1 ----
Medicine Name: Panadol
Sales Amount: Rs. 1350.00
Remaining Stock: 5

Warning: Low Stock! Restocking Required.

---- Medicine 2 ----
Medicine Name: Calpol
Sales Amount: Rs. 500.00
Remaining Stock: 30

Stock Status: Sufficient

=== Daily Pharmacy Sales Report ===

Total Medicines Entered: 2
Medicines Successfully Processed: 2
Total Pharmacy Revenue: Rs. 1850.00
Medicines Requiring Restocking: 1
==================================
```

**Invalid medicine count example:**

```text
Enter the number of medicines: abc
Invalid Input! Number of medicines must be a whole number of at least 1.
```

**Insufficient stock example:**

If the available stock is 5 and the quantity sold is 10, the program prints:

```text
Insufficient stock!
Available stock: 5
Requested quantity: 10
Sale could not be processed.
```

That medicine is not counted as successfully processed.

## Author

**Abdul Rafay**

Created as part of the Python Conditions & Loops Assessment.

---
