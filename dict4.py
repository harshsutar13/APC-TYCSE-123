#4. Create a dictionary containing student marks. Update the marks of a specified student.

dict1 = {
    "s1":95,
    "s2":92,
    "s3":90,
    "s4":85,
    "s5":80
}

key = input("Enter student name : ")
flag=False
for i in dict1:
    if key == i :
        print("Student:  Marks:")
        print(key,dict1[key])

        new_mark=int(input("Enter New Marks :"))
        dict1[key]=new_mark
        print("Marks Changed")
        flag=True

if flag == False :
    print("Name not found")

print(dict1)