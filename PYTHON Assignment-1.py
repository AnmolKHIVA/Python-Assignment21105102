print("Question-1")

number1=int(input("enter first number:"))
number2=int(input("enter second number:"))
number3=int(input("enter third number:"))
avg=(number1+number2+number3)/3
print("Average is:",avg)


print("Question:2")

standard_deduction=10000
additional_deduction=3000
rate=0.2
gross_income=float(input("Enter your gross income in dollars:\n"))
dependents=int(input("Enter number of dependents:\n"))
taxable_income=gross_income-standard_deduction-(dependents*additional_deduction)
tax=taxable_income*rate
print("Your total tax:\n",tax)


print("QUESTION-3")

student_list=[]
sid=int(input("Enter your student id:\n"))
name=str(input("Enter your name:\n"))
gender=str(input("Enter your gender:\n"))
course_name=input("Enter your course name:\n")
cgpa=float(input("Enter your CGPA:\n"))
student_list.append(sid)
student_list.append(name)
student_list.append(gender)
student_list.append(course_name)
student_list.append(cgpa)
print(student_list)


print("Question:4")

Marks=[8,9,5,6,4]
Marks.sort()
print(Marks)
Marks.sort(reverse=True)
print(Marks)


print("Question-5")

color =['Red','Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
color.pop(3)
color.insert(3,'purple')
print(color)















