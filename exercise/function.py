# def add(x,y):
#     print(x + y)

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# add(a,b)


# def add():
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     print(a + b)

# add()

# def take_value():
#     p=10
#     t=10
#     r=10
#     return [p,t,r] 
# def calculate():
#     # res =take_value()
#     # a = res[0]
#     # b = res[1]
#     # c = res[2]
#     a, b, c = take_value()
#     return (a*b*c)/100

# def display():
#     print("The simple interest is:", calculate())

# display()


# def take_mark():
# 	nep=float(input("Enter Nepali mark: "))
# 	eng =float(input("Enter English mark: "))
# 	math =float(input("Enter Math mark: "))
# 	sci =float(input("Enter Science mark: "))
# 	soc =float(input("Enter Social mark: "))
# 	return [nep, eng, math, sci, soc]

# def total():
# 	nep, eng, math, sci, soc = take_mark()
# 	return nep + eng + math + sci + soc 


# def percentage():
# 	t = total()
# 	p =t/5
# 	return [t,p]


# def division():
# 	grade =""
# 	result = percentage()
# 	per = result[1]
# 	tot = result[0]

# 	if per >= 80:
# 		grade = "Distinction"
# 	elif per >= 60:
# 		grade = "First Division"
# 	elif per >= 45:
# 		grade = "Second Division"
# 	elif per >= 32:
# 		grade = "Third Division"
# 	else:
# 		grade = "Fail"

# 	return [grade,per, tot]

# def result():
# 	res = division()
# 	print("Total Marks:", res[2])
# 	print("Percentage:", res[1])
# 	print("Division:", res[0])


# result()



# def login():
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username == "admin" and password == "password123":
#         return True
#     else:
#         return False
    

# print(login())
# name =""
# def message():
#     global name
#     name =input("Enter your name: ")
#     return name




# if name == message():
#     print("Welcome, admin!")
# else:
#     print("Access denied.")
#     question = input("Do you want to try again? (yes/no): ")
#     if question.lower() == "yes":
#         message()
#     else:
#         print("Goodbye!")

# users=["ram","sita","gita","hari","shyam","ram",'hari']

# def search_names(name):
#     find_user=[]
#     for user in users:
#         if user == name:
#             find_user.append(user)
        
        
#     if len(find_user)>0:
#         return find_user
#     else:
#         return "User not found"


# name = input("Enter name to search: ")
# res = search_names(name)
# print(res)


# def add(x,y):
#     return x + y

# result = add(5,10)
# print("The sum is:", result)


# def my_asc(*numbes):
#     num=list(numbes)
#     new_asc_order=[]
#     first =num[0]
#     for n in num:
#         if n<first:
#             new_asc_order.insert(0,n)
    
#     print(new_asc_order)
    
# my_asc(9,6,7,8,2)


# data=[23,1,2,45,67,89,12]
