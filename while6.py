# Write a PYTHON program to print sum of even numbers up to n

n = int(input("Enter the No. : "))

res =0
i=0
while(i <= n):
    res+=i
    i+=2

print(res)