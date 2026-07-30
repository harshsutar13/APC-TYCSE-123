#Write a PYTHON program to print sum of odd numbers up to n

n = int(input("Enter the No. : "))

res =0
i=1
while(i <= n):
    res+=i
    i+=2

print(res)