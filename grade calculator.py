marks = int(input("Enter your marks: "))

# Grading system
if marks >= 90 and marks <= 100:
    grade = "A+"
elif marks >= 80 and marks <= 89:
    grade = "A"
elif marks >= 70 and marks <= 79:
    grade = "B"
elif marks >= 60 and marks <= 69:
    grade = "C"
elif marks >= 50 and marks <= 59:
    grade = "D"
elif marks < 50:
    grade = "F"
else:
    grade = "Invalid marks! Please enter 0-100 only."

# Result print karna
print("Your Grade is:", grade)