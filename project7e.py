import datetime
import time
import math
import uuid

class time:
    
    def show_now(self):
        new=datetime.datetime.now()

        print("cuurent date & time :", new.strftime("%d-%m-%Y %H:%M:%S"))
    
    def date(self):
        try: 
            d1 = input("Enter the first date (YYYY-MM-DD) :")
            d2 = input("Enter the second date (YYYY-MM-DD) :")
            dt1 = datetime.datetime.strptime(d1,"%Y-%m-%d").date()
            dt2 = datetime.datetime.strptime(d2,"%Y-%m-%d").date()
            print("Diffrence :",dt1-dt2)
        except:
            print("Invalid Format ! Use YYYY-MM-DD.")
            
    def formate_date(self):
        try:
            d = input("Enter a date (YYYY-MM-DD)")
            t = input("Enter a formate (e.g. %d/%m%d)")
            dt = datetime.datetime.strptime(d ,"%Y/%m%d")
            print("formated date :",dt.strftime(f))
        except:
            print("invalid formated !")
            
    def stop_watch(self):
        input("Press enter to start stopwatch")
        a = time.time()
        input("Press enter to start stopeatch")
        b = time.time()
        
        diffrence = a - b
        h, rem = divmod(int(diff), 3600)
        m, s = divmod(rem, 60)
        print(f"Time Taken : {h}h {m}m {s}s ({diff:.2f} seconds)")
        
        
           
class Maths():
    
    def fac(self):
        try:
            n = int(input("Enter a Number : "))
            print("Factorial : ", math.factorial(n))
        except:
            print("Invalid input! Please enter an integer.")
            
    def Com_Interes(self):
        
        try:
            p = float(input("Enter principal amount : "))
            r = float(input("Enter rate of Interest (%) : "))
            t = float(input("Enter time (in years) : "))
            amt = p * ((1 + r / 100) ** t)
            ci = amt - p
            print("Compound Interest : ", round(ci, 2))
            print("Total Amount : ", round(amt, 2))
        except:
            print("Invalid input! Please enter numeric values.")    
    
class Random():
        def number(self):
           try:
               a = int(input("Enter the start range : "))
               b = int(input("Enter the end range : "))
               print("Random Numbers : ", random.randint(a, b))
           except:
               print("Invalid Input! Please Enter Correct Numbers.")

        def list_(self):
           try:
               sz = int(input("Enter the size of list : "))
               a = int(input("Enter the start range : "))
               b = int(input("Enter the end range : "))
               print("random List : ", [random.randint(a, b) for _ in range(sz)])
           except:
               print("Invalid Input! Kindly Enter Valid Numbers!")

        def password(self):
           try:
               ln = int(input("Enter the length of password : "))
               if ln <= 0:
                   print("Password Length Must be Greater than 0.")
                   return
               chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
               pw = "".join(random.choice(chars) for _ in range(ln))
               print("Random Password :", pw)
           except:
               print("Invalid input! Please enter a valid number.")

        def otp(self):
           print("Random Otp : ", "".join(str(random.randint(0, 9)) for _ in range(6)))
           
class Files():
    def create(self):
        try:
            name = input("Enter the file name : ")
            open(name, "w").close()
            print("File Created Successfully!")
        except:
            print("Error Occured!")

    def write(self):
        try:
            name = input("Enter the file name : ")
            data = input("Enter the data to write : ")
            with open(name, "w") as f:
                f.write(data)
            print("Data Written Successfully!")
        except:
            print("Error occured!")

    def read(self):
        try:
            name = input("Enter file name : ")
            if os.path.exists(name):
                with open(name, "r") as f:
                    print("File Data : \n", f.read(), "\n")
            else:
                print("File Not Found!")
        except:
            print("Error Occured!")

    def append(self):
        try:
            name = input("Enter file name: ")
            data = input("Enter data to append: ")
            with open(name, "a") as f:
                f.write("\n" + data)
            print("Data appended successfully!\n")
        except:
            print("Something went wrong while appending to the file.")

    
    
    
d = time()    


while True:    
    print("="*25)
    print("Welcome to Multiple toolkit")
    print("="*25)
    
    print("\n choose an option :")
    print("1. Date and Time Oprations ")
    print("2. Mathematics Oprations")
    print("3. Random date Generation")
    print("4. Generate Unique Identifier (UUID)")
    print("5. File Oprations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    
    choice = int(input("Enter your choice :"))
    
    if choice == 1:
        
        print("\n Date and Time Oprations: ")
        print("1. Display current date and time")
        print("2. Calculate deffernce between two date/time")
        print("3. Formate date into custom formate")
        print("4. Stopwatch")
        print("5. Back to main Menu")
        
        ch = int(input("Enter your choice :"))    
        
        if ch==1:
            d.show_now()
        elif ch==2:
            d.date()    
        elif ch==3:
            d.formate_date()
        elif ch==4:
            d.stop_watch()
        elif ch==5:
            continue
        
    elif choice == 2:
        m = Maths()
       
        print("\nMathematical Operations : ")
        print("1. Calculate Factorial.")
        print("2. Solve Compound Interest.")
        print("3. Back to Main Menu.")
        
        sub = int(input("\nEnter Your Choice : "))
        
        if sub==1:
            m.fac()
        elif sub==2:
            m.Com_Interes()
        elif sub==3:
            continue
        
    elif choice == 3:
        r = RandomGen()
        while True:
            print("\nRandom Data Generation : ")
            print("1. Generate Random Number.")
            print("2. Generate Random List.")
            print("3. Generate Random Password.")
            print("4. generate Random Otp.")
            print("5. Back To Main Menu.")
            sub = int(input("\nEnter Your Choice : "))
            if sub == 1:
                r.number()
            elif sub == 2:
                r.list_()
            elif sub == 3:
                r.password()
            elif sub == 4:
                r.otp()
            elif sub == 5:
                break
            
    elif choice == 4:
        print("\nGenerate Unique Identifier (UUID):")
        print("Generated UUID:", uuid.uuid4(), "\n")
    
    elif choice == 5:
        f = Files()
        while True:
            print("\nFile Operations Custom Module:")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            print("5. Back to Main Menu")
            sub = int(input("Enter Your Choice : "))
            if sub == 1:
                f.create()
            elif sub == 2:
                f.write()
            elif sub == 3:
                f.read()
            elif sub == 4:
                f.append()
            elif sub == 5:
                break

                
    elif choice == 6:
        mod = input("Enter module name to explore: ")
        try:
            m = __import__(mod)
            print(f"\nAttributes of {mod}:")
            print(dir(m))
        except:
            print("Module not found!")

    elif choice == 7:
        print("Exiting... Thank you for using Multi-Utility Toolkit!")
        break
    else:
        print("Invalid Choice! Please try again.")