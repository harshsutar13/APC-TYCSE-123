#Write a short PYTHON program to check weather the 
#     square root of number is prime or  not.

n = int(input("Enter the number: "))

res = n ** 0.5

if res == int(res):
    num = int(res)

    if num < 2:
        print("Given number's square root is Not Prime")
    else:
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break

        if flag:
            print("Given number's square root is Prime")
        else:
            print("Given number's square root is Not Prime")
else:
    print("Given number's square root is Not Prime")