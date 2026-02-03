students = []

while True:
    print("welcome to our progarmme\n")
    
    print("\n enter 1 to add student ") 
    print("enter 2 to view student")
    print("enter 3 to delete student")
    print("enter 4 to update student")
    print("enṭer 0 to exit\n")
    
    choice = int(input("enter your choice : "))
    
    if choice == 1:
        id = int(input("enter student id : "))
        name = input("enter student name : ")
        age = int(input("enter student age : "))
        
        student = {
            "id" : id,
            "name":name,
            "age":age 
        }
        
        students.append(student)
        
        print("\n student add successfully\n")
        
    elif choice == 2:
        # stid = int(input("enter student to view :"))
        
        for st in students:
            # if st["id"]==stid:
                print(f"id : {st["id"]} name : {st["name"]} age : {st["age"]}")
            
    elif choice == 3:
        stid = int(input("enter student id to delet : "))
        
        for st in students:
            if st["id"] == stid:
                students.remove(st)
                
                print("\n student removed successfully : \n")
                
    elif choice == 4:
        stid = int(input("Enter student id to update"))
        
        for st in students:
            if st["id"]==stid:
                st["name"] = input("enter student name : ")
                st["age"] = int(input("enter student age: "))
                
    elif choice == 0:
        print("\n thank you !")
        break

    else:
        print("\n choice invalid \n")
         
         