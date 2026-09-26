"""
Student Result and Scholarship Eligibility Library
Calculates total, average, grade, pass/fail and scholarship status
"""


def calculate_total_and_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, round(average, 2)


def get_grade(average):
    if average >= 80: return "A"
    elif average >= 70: return "B"
    elif average >= 60: return "C"
    elif average >= 50: return "D"
    else: return "F"


def check_pass(average, marks):
    return "PASS" if average >= 50 and all(m >= 50 for m in marks) else "FAIL"


def check_scholarship(status, average, age):
    return "YES" if status == "PASS" and average >= 80 and age <= 25 else "NO"


def calculate_fee(scholarship, base_fee=5500):
    discount = base_fee * 0.5 if scholarship == "YES" else 0
    return base_fee, discount, base_fee - discount


def process_student(name, age, marks):
    total, average = calculate_total_and_average(marks)
    grade = get_grade(average)
    status = check_pass(average, marks)
    scholarship = check_scholarship(status, average, age)
    base_fee, discount, final_fee = calculate_fee(scholarship)
    return {
        "Name": name, "Age": age, "Total": total,
        "Average": average, "Grade": grade, "Status": status,
        "Scholarship": scholarship, "Final Fee": final_fee
    }