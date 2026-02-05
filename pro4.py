array=[]

while True:
    
    
    print("welcome to data Analyzer and Transformer program!")
    print()
    
    print("main menu:")
    print()
    
    print("1. Input data")
    print("2. Display data summery (Built in functions)")
    print("3. calculate factorial (recursion)")
    print("4. Filter Data by threhold (lambda funcation) ")
    print("5. sort data ")
    print("6. Display Data Statitics (return Multiple values)")
    print("7. exit program")
    
    choice = int(input("Enter your choice: "))
    print()
    
    if choice == 1:
        num = int(input("Enter data for 1D array (separate by spaces): "))
        for i in range(num):
            value = float(input(f"Enter value {i+1}: "))