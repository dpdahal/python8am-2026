# What is loop?

# A loop is a sequence of instructions that is repeated 
# until a certain condition is met.

# type of loop
# for -> list,tuple,set
# while -> condition apply
# nested loops

# x=1

# while x<=10:
#     print(x)
#     x+=1


# x=10

# while x>=1:
#     print(x,end=" ")
#     x-=1


# x=1

# while x<=10:
#     if x%2==0:
#         print(x)
#     x+=1


# data=['ram','hari','gita']

# x=0

# while x<len(data):
#     print(data[x])
#     x+=1

# for name in data:
#     print(name)

# x=1
# num =int(input("Enter a number: "))

# while x<=10:
#     print(f"{num}x{x}={num*x}")
#     x+=1


# 1-10 total sum

# x=1
# total=0

# while x<=10:
#     total+=x
#     x+=1

# print("Total sum is:",total)

# users=['ram','hari','gita','sita','laxmi']

# for name in users:
#     if name=='ram' or name=='gita':
#         print(name)


# only print ram,gita,laxmi

# sentence="we are learning python programming"
# only print vowels letters

# for ab in sentence:
#     if ab in 'aeiou':
#         print(ab)

# users=[
#     {"name":'admin','address':'ktm'},
#     {"name":'ram','address':'pokhara'},
#     {"name":'gita','address':'bhaktapur'},
#     {"name":'sita','address':'bkt'},
#     {"name":'hari','address':'ktm'},
# ]

# for user in users:
#     print(user['name'])

users=[
    {"name":'admin','password':'admin002'},
    {"name":'ram','password':'ram002'},
    {"name":'gita','password':'gita002'},
   
]

username =input("Enter your username: ")
password =input("Enter your password: ")

is_login=False

for user in users:
    if user['name']==username and user['password']==password:
        print("Login successful")
        is_login=True
    

if not is_login:
    print("Invalid username or password")




students=[
    {'name':'ram','gender':'male','status':True},
    {'name':'hari','gender':'male','status':False},
    {'name':'sita','gender':'female','status':True},
    {'name':'rita','gender':'female','status':True},
    {'name':'laxmi','gender':'female','status':False},
]
# total_user=?
# total_active_user=?
# total_inactive_user=?
# total_active_male=?
# total_active_female=?
# total_inactive_male
# total_inactive_female

# search name
