#2. Create a dictionary containing employee information and display the value associated with a specified key.

dict1 = {
    "ID":123,
    "Name":"Harsh",
    "dept":"CSE",
    "salary":100000
}

key = input("Enter key to find : ")

for i in dict1:
    if key == i :
        print(key,dict1[key])

    else :
        print("Key not found")