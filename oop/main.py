# what is oop?
# oop stands for object oriented programming
#  what class?
# class is a blueprint for creating objects
# what object
# object is an instance of a class
#  properties and methods
#  properties -> attributes
#  methods -> behaviour
# x=10 variable is an object of int class
# def info():
#     print("this is a function")

# class TV:
#     model = "LG"

#     def play(self):
#         print("playing TV")
# t = TV()
# print(t.model)
# t.play()


# class Calculator:
#     def add(self,x,y):
#         return x+y
#     def sub(self,x,y):
#         return x-y
#     def mul(self,x,y):
#         return x*y
#     def div(self,x,y):
#         if y==0:
#             return "cannot divide by zero"
#         return x/y

# cal = Calculator()
# print(cal.add(10,5))
# print(cal.sub(10,5))
# print(cal.mul(10,5))
# print(cal.div(10,5))



# class TV:
#     model = "LG"

#     def info(self):
#         print(self.model)
# t = TV()
# t.info()


# what is self?
# self is a reference to the current instance of the class


# class Students:
#     s_list=['ram','shyam','hari']

#     def show(self):
#         for name in self.s_list:
#             print(name)

#     def add(self,name):
#         self.s_list.append(name)

#     def delete(self,index):
#         self.s_list.pop(index)

#     def update(self,index,new_name):
#         self.s_list[index]=new_name


# sInstance = Students()
# sInstance.add('gopal')
# sInstance.delete(1)
# sInstance.update(0,"sita")
# sInstance.show()

# what is constructor? or dunder method 
# constructor is a special method that is called when an object is created

# class TV:
#     def __init__(self):
#        print("constructor called")

# t = TV()

# t.model = "LG"
# print(t.model)


# class TV:
#     def __init__(self,name,model):
#        print(name,model)

# t = TV("LG","OLED")


# class TV:
#     def __new__(cls):
#         print("i am new method")
#         return super().__new__(cls)
    
#     def __init__(self):
#        print("i am constructor")

#     def info(self):
#         print("this is a TV")

#     def __str__(self):
#         pass

#     def __repr__(self):
#         pass

#     def __add__(self,other):
#         pass

#     def __del__(self):
#         print("i am destructor")

# t = TV()
# t.info()


# class Students:
#     total =0
#     def __init__(self,name):
#        Students.total+=1


# s1 = Students("ram")
# s2 = Students("shyam")
# s3 = Students("hari")

# print(s1.total)


# public, private and protected members

# public members are accessible from anywhere
# private members are accessible only within the class
# protected members are accessible within the class and its subclasses

# class TV:
#     __model = "LG"

#     def info(self):
#         print(self.__model)

# obj = TV()
# obj.info()

# what is setter and getter?
# class TV:
#     __model = "LG"

#     def get_model(self):
#         return self.__model
    
#     def set_model(self,model):
#         self.__model = model

# obj = TV()
# print(obj.get_model())
# obj.set_model("Samsung")
# print(obj.get_model())



# class TV:
#     __model = "LG"

#     @property
#     def model(self):
#         return self.__model
    
#     @model.setter
#     def model(self,new_model):
#         self.__model = new_model

# obj = TV()
# obj.model = "Samsung"
# print(obj.model)




# what is static method and class method?
# static method is a method that belongs to the class rather than 
# the instance of the class
# class TV:
#     name ='LG'
    
#     @staticmethod
#     def info():
#         print("this is a ",TV.name)
# TV().info()
# what is class decorator?
# what is property decorator?



# what is inheritance?
# inheritance is a mechanism of acquiring properties and methods of a class
# that is inherited by another class(parent child relationship)

# class Laptop:
#     def brand(self,name):
#         print("this is a ",name," laptop")

#     def price(self,new_price):
#         print("the price of this laptop is ",new_price,"$")

#     def model(self,model_name):
#         print("the model of this laptop is ",model_name)

  

# class Dell(Laptop):
#     pass
    

# obj = Dell()
# obj.brand("Dell")
# obj.price(1000)
# obj.model("inspiron")
# class Mac(Laptop):
#     pass

# obj2 = Mac()
# obj2.brand("Mac")
# obj2.price(2000)
# obj2.model("Macbook Pro")



# class Laptop:
#     def __init__(self,name):
#         print("this is a ",name," laptop")

        
#     def brand(self,name):
#         print("this is a ",name," laptop")

    

# class Dell(Laptop):
#     def __init__(self,name,price):
#         # Laptop.__init__(self,name)
#         super().__init__(name)
#         print("the price of this laptop is ",price,"$")
    

# obj = Dell("Dell",1000)
# obj.brand("Dell")


# class A:
#     def __init__(self,name):
#         print("this is a ",name," laptop")
        
# class B:
#     def __init__(self,name):
#         print("Hello",name," laptop")

#     def brand(self,name):
#         print("this is a model ",name," laptop")
    

# class Dell(A,B):

#     def __init__(self,name,price):
#         # Laptop.__init__(self,name)
#         # super().__init__(name)
#         A.__init__(self,name)
#         B.__init__(self,name)
#         print("the price of this laptop is ",price,"$")
    

# obj = Dell("Dell",1000)


class Apple:
    __price = 10

    @property
    def price(self):
        return f"the price of this apple is {self.__price} $"
    
    @price.setter
    def price(self,new_price):
        self.__price = new_price

    @classmethod
    def info(cls):
        print("this is a apple class")



obj = Apple()
obj.price = 20
print(obj.price)