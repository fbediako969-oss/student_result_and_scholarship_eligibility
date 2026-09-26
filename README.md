# student_result_and_scholarship_eligibility
Student Result and Scholarship Library

A Python library that calculates total marks, average, grade and pass or fail status using logical operators. It checks scholarship eligibility for students with average of eighty and above and age twenty five or younger, and computes final tuition after fifty percent discount. Built with modular reusable functions for academic systems.

Features
- Calculate total marks and average
- Determine grade and pass or fail status
- Check scholarship eligibility using logical operators
- Compute final tuition fee after scholarship discount

Installation

git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME

Usage

from student_lib import calculate_result, check_scholarship, calculate_fee

# Example
total, average, grade, status = calculate_result([85, 90, 78, 88])

eligible = check_scholarship(average, 22, status)
# Returns True if average >= 80 and age <= 25 and passed

final_fee = calculate_fee(10000, eligible)
# Returns 5000 if eligible, else 10000

print(total, average, grade, status, eligible, final_fee)

Functions
- `calculate_result(marks)` - Returns total, average, grade, status
- `check_scholarship(average, age, status)` - Returns True or False
- `calculate_fee(tuition, is_eligible)` - Returns final fee after discount

Project URL
`https://github.com/YOUR-USERNAME/YOUR-REPO-NAME`
