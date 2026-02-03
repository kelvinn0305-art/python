# Basic I/O functions

# print("hello world",end="&")
# print("welcome")

# A = input("Enter your input: ")
# print(A)

# Types of Comments

# 1.Single-line Comment

# 2.Multi-line Comment

# A = input("Enter your input: ")
# print(A)

# 2.Multi-line Comment

'''habit = "Gambling"
del habit
print(habit)'''



# variable

# A="python"
# print(A)

# single quotes, double quotes, and triple quotes.

# A = 'python'
# print(A)

# A = "python"
# print(A)

# A = '''python
# data science'''
# print(A)

# # valid variable names
# samay = 12
# _rohit = 90.34
# rahul_sharma = 33

# # invalid variable names
# 5G = 22.33
# 9Mohit = 34
# @ronit = 11.45
# piyush patel = 85
# if = 20

# del object

# habit = "Gambling"
# del habit
# print(habit)

# Operator Precedence

# A = 1 + 2 * 3 / 4 ** 2
# print(A)  

# id() and type() functions


# a="python"
# print(id(a))

# a="python"
# print(type(a))

# string data type


# text = "Python"
# first_char = text[1:6] 
# print(first_char)

# A = len("text")
# print(A)

# A =  "PYTHON"
# print(A.lower())

# A =  "python"
# print(A.upper())

# A =  "python"
# print(A.title())

# A =  "python"
# print(A.capitalize())

# A =  "   python   "
# print(A.strip())

# A =  "python data science"
# print(A.split())

# A =  ["data","science"]
# print(''.join(A))

# A =  "python"
# print(A.find("n"))

# A =  "data science"
# print(A.replace("science", "data"))


# string formatting

# name = "kelvin" #using % oprerator
# age = 21

# formatted_string = "my name is %s my age is %d" % (name , age)
# print(formatted_string)

# name = "kelvin" #using str.format() method
# age = 21

# formatted_string = "my name is {} and I am {} years old.".format(name, age)
# print(formatted_string)

# name = "kelvin" #using f-strings
# age = 21

# formatted_string = f"my name is {name} and I am {age} years old."
# print(formatted_string)

# l = []
# t = ()
# s = {}
# d = {}

# print(type(l))
# print(type(t))
# print(type(s))
# print(type(d))

l = [60,50,40,30,20,10]

# print(l)

# print(l[1])
# print(l[-1])

# l[1] = "banana"
# print(l)#index add

# l.append("100")
# print(l)

# l.extend(["kelvin", 55.5])#multiple value add
# print(l)

# l.insert(3,"kelvin")
# print(l)

# del l[2]#del value
# print(l)

# count = l.index(True)
# print(count)
# print(l)

# l.remove(True) #element remove
# print(l)

# l.reverse() # all element reverse
# print(l)

# l.sort() #all element line by line
# print(l)

# l.copy() #all element 
# print(l)

# 1d array

# array = [10,20,30,40,50]
# print(array[3])

