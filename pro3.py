li = []

while True:

    print("welcome to the student data organizer!")
    print()

    print("select an option:")
    print("1. Add student data")
    print("2. Display all students")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Display subject offered")
    print("6. Exit")
    print()

    choice=int(input("Enter your choice: "))
    print()

    if choice==1:
        print("Enter student detail: ")
        stud={
            "studid":int(input("student ID: ")),
            "studname":input("Name: "),
            "studage":input("Age: "),
            "Studgrade":input("Grade: "),
            "studdob":input("Date of Birth:(YYY-MM-DD) "),
            "studsub":input("subjects (comma-separated): ")
        }
        print()
            
        li.append(stud)
        
        
        print("Student added successfully!")

    elif choice==2:
        print("Displaying all students:")
        for stud in li:
            print(f"ID: {stud['studid']} | Name: {stud['studname']} | Age: {stud['studage']} | Grade: {stud['Studgrade']} | DOB: {stud['studdob']} | Subjects: {stud['studsub']}")

    elif choice==3:
        studid=int(input("Enter student ID to update: "))
        for stud in li:
            if stud['studid']==studid:
                stud['studname']=input("Updated Name: ")
                stud['studage']=input("Updated Age: ")
                stud['Studgrade']=input("Updated Grade: ")
                stud['studdob']=input("Updated Date of Birth:(YYY-MM-DD) ")
                stud['studsub']=input("Updated subjects (comma-separated): ")
                
                print("Student information updated successfully!")
    elif choice==4:
        stuid =int(input("Enter student ID to delete:"))
        for stud in li:
            if stud ['studid']==studid:
                li.remove(stud)
                
                print("student deleted successfully!")
    elif choice==5:
        studid=int(input("Enter student ID to display subjects: "))
        for stud in li:
            if stud ['studid']==studid:
                print(f"Subject: {stud['studsub']}")
                
    elif choice==6:
        print("Exiting the program. Goodbye!")
        break
    
    else:
            print("Invalid choice! Please try again.")

      



