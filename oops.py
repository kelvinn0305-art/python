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
       
    
class bank:
    
    def __init__(self,name,accNum,balance):
        self.name=name
        self.accNum=accNum
        self.balance=balance
        
        print("accoumt created !")
        
    def getinfo(self):
        print("name :",{self.name},"account number )
        
        
    