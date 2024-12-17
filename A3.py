#curd operation on dictionary
import re
from prettytable import PrettyTable
table=PrettyTable()
numPattern = r'^[0-9]+$'
namePattern = r"^[A-Za-z]+(([' -][A-Za-z])?[A-Za-z]*)*$"
Stud = {}
g = ("dist", "a", "b", "c", "fail", "pass")
cat = ("open", "obc", "sc", "st", "nt", "ews")

def isValidName(name):
    if re.fullmatch(namePattern, name):
        return True
    else:
        return False
    
def isValidNum(n):
    if re.fullmatch(numPattern, n):
        return True
    else:
        return False
    
# Accept name
def acceptName():
    name = input("Enter Student Name: ")
    if isValidName(name):   
        return name
    else:
        print("\nInvalid Name.\n")
        return None

# Accept roll number
def acceptRollNo():
    rollNo = input("Enter Student Roll No: ")
    if isValidNum(rollNo):
        if rollNo in Stud:
            print("\nRoll No already exists. Please enter a different Roll No.\n")
            return None
        else:
            return rollNo
    else:
        print("\nInvalid Roll No.\n") 
        return None

# Accept age
def acceptAge():
    age = input("Enter Student Age: ")
    if age.isnumeric() and 6 < int(age) < 30:
        return age
    else:
        print("\nInvalid Age.\n")
        return None

# Accept grade
def acceptGrade():
    grade = input("Enter Student Grade ('dist', 'a', 'b', 'c', 'fail', 'pass'): ")
    grade=grade.lower()
    if grade in g:
        return grade
    else:
        print("\nInvalid Grade.\n")
        return None    
    
# Accept category
def acceptCat():
    cate = input("Enter Student Category ('open', 'obc', 'sc', 'st', 'nt', 'ews'): ")
    cate=cate.lower()
    if cate in cat:
        return cate
    else:
        print("\nInvalid Category.\n")
        return None
    
# Insert student details
def InsertStud():
    sid = acceptRollNo()
    if sid is None:
        return 0
    name = acceptName()
    if name is None:
        return 0
    age = acceptAge()
    if age is None:
        return 0    
    grade = acceptGrade()
    if grade is None:
        return 0
    category = acceptCat()
    if category is None:
        return 0
    Stud[sid] = {"Name": name, "Age": age, "Grade": grade, "Category": category}
    return 1
    
# Update the details
def updateStudDetails():
    sid = input("Enter the roll number of the student you want to update: ")
    if sid in Stud:
        print("1. Name\n2. Age\n3. Grade\n4. Category\n5. Roll Number")
        ch = input("Enter what you want to update from the above: ")
        if ch == "1":
            name = acceptName()
            if name:
                Stud[sid]["Name"] = name
                print("\nName updated successfully\n")
        elif ch == "2":
            age = acceptAge()
            if age:
                Stud[sid]["Age"] = age
                print("\nAge updated successfully\n")
        elif ch == "3":
            grade = acceptGrade()
            if grade:
                Stud[sid]["Grade"] = grade
                print("\nGrade updated successfully\n")
        elif ch == "4":
            category = acceptCat()
            if category:
                Stud[sid]["Category"] = category
                print("\nCategory updated successfully\n")
        elif ch == "5":
            nsid = acceptRollNo()
            if nsid:
                Stud[nsid] = Stud[sid]
                del Stud[sid]
                print("\nRoll number updated successfully\n")
        else:
            print("\nInvalid choice, please try again\n")
    else:
        print("\nStudent not found\n")

# Retrieve the data
def retrieveStud():
    sid = input("Enter the roll number of the student: ")
    if sid in Stud:
        table.field_names=["Roll No","Name","Age","Grade","Category"]
        table.add_row([sid,Stud[sid]["Name"],Stud[sid]["Age"],Stud[sid]["Grade"],Stud[sid]["Category"]])
        
        print(table)
        table.clear()
    else:
        print("\nStudent not found\n")

# Delete the student
def deleteStud():
    sid = input("Enter the roll number of the student: ")
    if sid in Stud:
        del Stud[sid]
        print("\nStudent deleted successfully\n")
    else:
        print("\nStudent not found\n")

# Show all students
def showAllStud():
    if len(Stud) == 0:
        print("\nNo students in the database\n")
    else:
        table.field_names=["Roll No","Name","Age","Grade","Category"]
        for sid, details in Stud.items():
            table.add_row([sid,details['Name'],details['Age'],details['Grade'],details['Category']])
        print(table)
        table.clear()

# Main menu-driven loop
while True:
    print("\n1. Add Student")
    print("2. Update Student")
    print("3. Retrieve Student")
    print("4. Delete Student")
    print("5. Show All Students")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        if InsertStud() == 1:
            print("\nStudent details inserted successfully\n")
    elif choice == "2":
        updateStudDetails()
    elif choice == "3":
        retrieveStud()
    elif choice == "4":
        deleteStud()
    elif choice == "5":
        showAllStud()
    elif choice == "6":
        break
    else:
        print("\nInvalid choice, please try again\n")
