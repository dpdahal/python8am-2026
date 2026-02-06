# obj =open("filehandling/students.txt", "w")
# obj.write("Hello Nepal")
# obj.close()

# obj =open("filehandling/students.txt", "a")
# obj.write("Hello Nepal \n")
# obj.close()


obj =open("filehandling/students.txt", "a")
name = input("Enter your name: ")
email = input("Enter your email: ")
address = input("Enter your address: ")
obj.write(f"{name}, {email}, {address}\n")
# print(obj.read())
# print(obj.readline())
# print(obj.readlines())
# obj.close()

# WAP to enter 5 subject marks from user and store it in marks.txt file

# ram, 98, 95, 93, 97, 96,


# regex 
# tkinter module