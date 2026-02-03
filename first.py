print('welcome to the interactive personal data collector!')
print()

name = input('please enter your name :')
age = int(input('please enter your age:'))
height = float(input('please enter your height in meters:'))
favoritenumber = int(input('please enter your favorite number:'))
print()

print('thank you! Here is the information you provided:')
print()

print("Name : ",name,"type :" ,type(name),"address :",id(name))
print("Age : ",age,"type :" ,type(age),"address :",id(age))
print("Height : ",height,"type :" ,type(height),"address :",id(height))
print("Favorite number :",favoritenumber,"type :",type(favoritenumber),"address :",id(favoritenumber))
print()

print("your birth year is approximately :",2025 - age)
print()


print("thank you for using the personal data collector. goodbye!")
