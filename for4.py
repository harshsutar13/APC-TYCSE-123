#Write a PYTHON program that prints  1 2 4 8 16 32 … n2

n = int(input("Enter the number :"))

for i in range(0,n+1):
    print(2**i)
