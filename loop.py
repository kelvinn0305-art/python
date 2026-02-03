# for i in range(5):
#     print("*")

# for i in range(1,6):
#     print("*"*i)

# for i in range(6,1,-1):
#      print(i)

# for i in range(5,0,-1):
#      print(str(i)*i)
     
# nested loop

# for i in range(1,6):
#      for j in range (1,i+1):
#           print(j,end=" ")
#      print()

# for i in range(6,1,-1):
#      for j in range (6,i-1,-1):
#           print(j,end=" ")
#      print()


print("Welcome to the patteren generator and Number Analzer!")
print()

print("Select an option:")
print("1. Generate a pattern")
print("2. Analyze a Range of numbers")
print("3. exit")

choice = int(input("Enter your choice: "))

if choice == 1:
     print("You chose to generate a pattern.")

elif choice == 3:
     print("Thank you for using the program. Goodbye!")
     exit()

choice2 = int(input("Enter the number of rows for the pattern: "))
print()


print("pattern:")

for i in range(choice,choice2+1):
    print("*"*i)
    print()
    
# print("Selct an option:")
# print("1. Generate a pattern")
# print ("2. Analyze a Range of Numbers")    
# print("3. exit")

# choice = int(input("Enter your choice:"))
# print()

