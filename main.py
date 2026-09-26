from student_result_scholarship_lib import process_student

name = input("Enter student's name: ")
age = int(input("Enter age: "))
marks = [
    int(input("Mathematics: ")),
    int(input("English Language: ")),
    int(input("Integrated Science: ")),
    int(input("Social Studies: "))
]

result = process_student(name, age, marks)
print("\n========== RESULT ==========")
for k, v in result.items():
    print(f"{k}: {v}")