# class car:
#     brandname="toyota"
#     modelname="fortuner"
    
# obj = car()

# print(obj.brandname)
# print(obj.modelname)

# EX.1

# class door:
#     __doortype=None
#     __windowtype=None
    
#     def setter(self,doortype,windowtype):
#         self._doortype=doortype
#         self._windowtype=windowtype
        
#     def getter(self):
#         print(self._doortype,self._windowtype)
        
# obj = door()
    
# obj.setter("wooden","steel")
# obj.getter()
    
#  EX.2

# class car:
#     __brandname=None
#     __colorname=None
#     __modelname=None
    
#     def setter(self,brandname,colorname,modelname):
#         self.__brandname=brandname
#         self.__colorname=colorname
#         self.__modelname=modelname
        
#     def getter(self):
#         print("brandname: ",self.__brandname,"\n""colorname: ",self.__colorname,"\n""modelname: ",self.__modelname)
        
# obj = car()

# obj.setter("maruti","white","i20")
# obj.getter()


# # EX.3

# class bank:
#     __accountname=None
#     __accountnumber=None
#     __bankbalance=None
    
#     def setter(self,accountname,accountnumber,bankbalance):
#         self.__accountname=accountname
#         self.__accountnumber=accountnumber
#         self.__bankbalance=bankbalance
        
#     def getter(self):
#         print("accountname: ",self.__accountname,"\n""accountnumber ",self.__accountnumber,"\n","bankbalance: ",self.__bankbalance)
        
        
# obj = bank()

# obj.setter("jay",123456789,120)
# obj.getter()

# # EX.4

# class student:
#     __studentname=None
#     __studentid=None
#     __studentmark=None
    
#     def setter(self,studentname,studentid,studentmark):
#         self.__studentname=studentname
#         self.__studentid=studentid
#         self.__studentmark=studentmark
        
#     def getter(self):
#         print("studentname :",self.__studentname,"\n","studentid :",self.__studentid,"\n","studentmark :",self.__studentmark)
        
# obj = student()

# obj.setter("kelvin",1,100)
# obj.getter()

# class person():
    
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def display(self):
#         print(self.name,self.age)
        
#     def __del__(self):
#         print("finished")  

# obj = person("kelvin",21)
# obj.display()

# obj1 = person("jay",21)
# obj1.display()
       
    

# Inheritance

#  singale inheritance  

# class animal:
#     def sound(self):
#         print("animal")
        
# class dog(animal):
#     def speaking(self):
#         print("break")
        
# obj = dog()


# obj.sound()
# obj.speaking()


#  multiple inheritance

# class animal:
    
#     def sound(self):
#         print("animal")
        
# class dog:
#     def speaking(self):
#         print("break")
        
# class cat(animal,dog):
#     def speaking1(self):
#         print("meow")
        
# obj = cat()

# obj.sound() 
# obj.speaking()
# obj.speaking1()

# multi level inheritance

# class animal:
#     def sound(self):
#         print("animal")
        
# class dog(animal):
#         def speaking(self):
#             print("beark")
            
# class cat(dog):
#          def speaking1(self):
#              print("meow")
             
# obj = cat()

# obj.sound()
# obj.speaking()
# obj.speaking1()


# hierarchical inheritance
      
# class  animal:
#     def sound(self):
#         print("animal")
        
# class dog(animal):
#     def speaking(self):
#         print("break")
        
# class cat(animal):
#     def speaking1(self):
#         print("meow")
        
# obj = cat()
# obj1 = dog()

# # obj.sound() 
# obj1.speaking()
# obj.speaking1()

# polymorphism 

# method overridng
# method overloading
# operator overloading

# method overriding

# class animal:
#     def sound(self):
#         print("animal")
        
# class dog(animal):
#     def sound(self):
#         print("dog")

# class cat(animal):
#     def sound(self):
#         print("cat") 
        
# obj = cat()

# obj.sound()


# overlodaing

# class math:
#     def __init__(self,marks=30):
#         self.marks=marks
    
#     def __add__(self,other):                                                                                                                           
#         return self.marks + other.marks
    
#     def __str__(self):
#         return str(self.marks)
# obj = math(20)
# obj1 = math(30) 
# obj2 = math(20)



class car:
    def __init__(self,brandname,modelname):
        self.brandname=brandname
        self.modelname=modelname
        
    def showcarinfo(self):
            print(f"the car brand is{self.brandname} and the model is {self.modelname}")
            
class mahindra(car):
    def __init__(self,brandname,modelname,turbo):
        super().__init__(brandname,modelname)
        self.turbo=turbo
        
    def showcarinfo(self):
        print(f"the car brand is {self.brandname} and the model is {self.modelname} and the turbo is {self.turbo}")
        
class toyota(car):
    def __init__(self,brandname,modelname,seats):
        super().__init__(brandname,modelname)
        self.seats=seats
        
    def showcarinfo(self):
        print(f"the car brand is {self.brandname} and the model is {self.modelname} and the seats no. is{self.seats}")
        
        
Bcars = []
Tcars = []
Mcars = []

while True:
    
    print("\n Enter 1 the add basic car ")
    print(" Enter 2 the add mahindar car ")
    print(" Enter 3 the add toyota car")
    print(" Enter 4 the show all cars")
    print(" Enter 5 to exit")
        
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        brandname = input("Enter the brand name: ")
        modelname = input("Enter the mdoel name: ")
         
        car1 = car(brandname,modelname)
        Bcars.append(car1)
        
    elif choice == 2:
        barndname = input("Enter the barnd name: ")
        modelname = input("Enter the model name:")
        turbo = input("turbo is avaiable yes/no :")
        
        car2 = mahindra(brandname,modelname,turbo)
        Mcars.append(car2)
        
    elif choice == 3:
        brandname = input("Enter the brandname : ")
        modelname = input("Enter the modelname : ")
        seats  = input("Enter the seats no. : ")
        
        cars3 = toyota(brandname,modelname,seats)
        Tcars.append(cars3)
        
    elif choice == 4:
        print(" Enter 1 the add basic car ")
        print(" Enter 2 the add mahindar car ")
        print(" Enter 3 the add toyota car")
        
        Achoice = int(input("Enter your choice"))
        
        if Achoice == 1:
             for car1 in Bcars:
                 car1.showcarinfo()
            
            
        elif Achoice == 2:     
             for car2 in Mcars:
                car2.showcarinfo()
                
        elif Achoice == 3:       
             for car3 in Tcars:
                 car3.showcarinfo()
                 
        else: 
            print("\n anvalid choice")
            
    elif choice == 0:
        print("\n exiting ")
        break
        
    else:
        print("\n invalid choice \n")

            
        
        
        
        
        
        