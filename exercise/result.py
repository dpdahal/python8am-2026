num =int(input("Enter number of students: "))
x=1 
students_marks=[]
while x<=num:
    print(f"=====Roll no: {x}========")
    nep=int(input("Enter nep mark: "))
    eng=int(input("Enter eng mark: "))
    mat=int(input("Enter mat mark: "))
    sic=int(input("Enter sic mark: "))
    com=int(input("Enter com mark: "))
    total = nep+eng+mat+sic+com 
    students_marks.append(total)
    x+=1

for total in students_marks:
    per = total/5
    grade =""
    if per>35 and per<60:
        grade="C"
    elif per>60 and per<80:
        grade="B"
    elif per>80  and per<=100:
        grade="A"
    else:
        grade="None"

    print(f"Total: {total} percentage: {per} Grade: {grade}")