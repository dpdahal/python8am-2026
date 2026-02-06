# What is function?
# A function is a block of organized, 
# reusable code that is used to perform a single, related action. 

# type of function
# 1. Built-in functions: print(), len(), type(), etc.
# 2. User-defined functions: Functions created by the user using the def keyword.

# def message():
#     print("Hello python ")


# message()

# function with parameter

# def message(name):
#     print("Hello ",name)


# message('python')
# message('java')
# message('c++')


# a=5
# b=6 
# print(a+b)

# c=5
# d=7

# def add(a,b):
#     print(a+b)

# add(6,7)
# add(8,7)


# def add(a,b,c):
#     print(a+b)

# add(6,7,9,89)


# def students(names):
#     print(names)


# students(["ram","sita"])


# def total(nums):
#     print(sum(nums))

# total([1,2,3,4,5])


# def total(nums):
#     t=0
#     for a in nums:
#         t+=a  
#     print(t)

# total([1,2,3,4,5])


# optional parameter

# def user(name,age=0):
#     print(name)
#     print(age)

# user('ram',20)

# *args 
# **kwargs


# def students(*args,**kwargs):
#     print(args)
#     print(kwargs)


# students("ram","sita",'hari','govind',name='sophia',age=50)

# 5 -> 120

# 5-1 =4*5=20
# 4-1=3*20=60
# 3-1=2*60=120


# def test():
#     print("Hello test")
#     test() 

# test()

# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)

# print(fac(5))


# def hello():
#     return "Hello python"
#     return "Hello java"

# print(hello())
# def add(x,y):
#     sm = x+y 
#     sb = x-y
#     return [sm, sb]

# print(add(5,6))


# def add(x,y):
#     sm = x+y 
#     return sm

# total =add(6,8) 
# print(total(6,9))

# def add(x,y):
#     return x+y 


# def total():
#     print(add(8,7))

# total()


# def add(x,y):
#     return x+y 


# def total(a,b,callback):
#     print(callback(a,b))

# total(6,8,add)


# total =lambda x,y: x+y
# print(total(5,8))

# def message():
#     yield "Hello python"
#     yield "Hello java"
#     yield "Hello c++"


# a = message()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))




# function scope 
# 1. Local scope
# 2. Global scope

x=10

def info():
    global x
    x=x+50
    print(x)
    
info()
print(x)