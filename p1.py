while True:
    print("welcome to the pattern generator number analyzer!")
    print()
    
    print("1 genrate a pattern")
    print("2 Analyze a name of numbers")
    print("3 exit")
    print()
    
    choice = int(input("enter your choice:"))

    if choice == 1:
        for i in range(0,6):
            print("*"*i)
    elif choice==2:
        start = int(input("enter the start of Range:"))
        end = int(input("enter the end of Range:"))
        for i in range(start,end):
            if i%2==0:
                print(i,"is a even number")
            else:
                print(i,"is a odd number")
                
        sum = 0
        num = 10
            
        while num <=15:
         sum += num
         num += 1
                
        print("the sum of numbers from 10 to 15 is:",sum)
        print()
    elif choice==3:
        print("exting the program!")
        break 
    else:
        print("exiting the program!")
                
    