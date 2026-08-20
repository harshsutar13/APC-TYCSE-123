#5. Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.

s1={"Harsh","Prithvi","Yash","Atharv"}

name = input("Enter Name to check : ")

flag = 0
for i in s1:
    if i == name:
        print("name found : ",name)
        flag = 1
        break;

if flag == 0:
    print("Name Not Found")