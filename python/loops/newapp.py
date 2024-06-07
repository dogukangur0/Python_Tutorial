isContinue = "y"


students=[]

while isContinue!="n":
    studentNo = int(input("Enter the student number:"))
    studentName = input("Enter the student name:")
    studentSurname = input("Enter the student surname:")

    students.append({
        "student_no":studentNo,
        "student_name":studentName,
        "student_surname":studentSurname
    })

    isContinue=input("is Continue :(y/n)")

if(isContinue!="y"):
    for a in students:
        print(f"{a["student_no"]} {a["student_name"]} {a["student_surname"]}") 
